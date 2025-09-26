conda init 2>&1 1>/dev/null
conda activate base
uvicorn app_api:app --port 8080 2>&1 | tee raw_logfile_api.log
