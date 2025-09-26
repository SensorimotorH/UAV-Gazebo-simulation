import asyncio
from fastapi import BackgroundTasks, FastAPI
from pydantic import BaseModel
from sse_starlette import EventSourceResponse

# from static_file import static_file_router, templates


from backend import product_apirouter
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager
from agent_config import conf
import os
from logic import Agent


class InputItem(BaseModel):
    input_str: str


agent: Agent = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    # print("Run at startup!")
    # yield
    # print("Run on shutdown!")
    global agent
    # Load the ML model
    # ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    agent = Agent()
    print("Run at startup!")
    yield
    # Clean up the ML models and release the resources
    # ml_models.clear()
    # agent = Agent()
    print("Run on shutdown!")


origins = [
    "http://localhost:5174",
]

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.mount("/static", static_file_router, name="static")
app.mount("/chat", StaticFiles(directory="front-file/dist", html=True), name="static")
app.mount(
    "/static_file",
    StaticFiles(directory="static_file/img", html=False),
    name="static_file",
)


@app.get("/map/image")
async def get_image():
    image_dir = "static_file/img"  # 图片目录
    images = os.listdir(image_dir)
    if not images:
        return JSONResponse(content={"error": "No images found"}, status_code=404)

    # 获取最新的图片
    images.sort(
        key=lambda img: os.path.getmtime(os.path.join(image_dir, img)), reverse=True
    )
    latest_image = images[0]

    # 构造图片的URL
    image_url = f"/static_file/{latest_image}"
    return {"url": image_url}


@app.get("/map/object")
async def get_object():
    global agent
    if agent is None:
        agent = Agent()
    return agent.agent_object_output()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get(conf.get("LogicUrl", "agent_output_url"))
async def root(request: Request):

    async def event_generator(request: Request):
        while True:
            if await request.is_disconnected():
                print("连接已中断")
            else:
                data = None
                if agent is not None:
                    data = next(agent.agent_output())
                else:
                    data = "agent is None"
                    break
                yield {
                    "event": "message",
                    "retry": 15000,
                    "data": data,
                }
            await asyncio.sleep(0.5)

    g = event_generator(request)
    return EventSourceResponse(g)


@app.post(conf.get("LogicUrl", "agent_input_url"))
async def input(input_item: InputItem, background_tasks: BackgroundTasks):
    global agent
    if agent is None:
        agent = Agent()
    if not agent.is_running():
        background_tasks.add_task(agent.start)
    return agent.agent_input(input_str=input_item.input_str.strip())
