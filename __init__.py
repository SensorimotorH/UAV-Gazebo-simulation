data_str = "fnd17_oxlcxspebq, fnd17_shsoutbs,fnd17_oxlcxspebq, fnd28_value_05191q, fnd17_oxlcxspebq, fnd28_value_05192q,fnd17_oxlcxspebq, fnd28_value_05301q,fnd17_oxlcxspebq, fnd28_value_05302,fnd17_pehigh, fnd17_pelow,fnd17_priceavg150day, fnd17_priceavg200day,fnd17_priceavg150day, fnd17_priceavg50day,fnd17_priceavg200day, fnd17_priceavg50day,fnd17_pxedra, fnd17_tbea,fnd17_pxedra, fnd28_newa3_value_18191a,fnd17_pxedra, fnd28_newa3_value_18198a,fnd17_pxedra, fnd28_value_02300a,fnd17_pxedra, fnd28_value_05302,fnd17_pxedra, mdl175_ebitda,fnd17_pxedra, mdl175_pain"
data_list = [i.strip() for i in data_str.split(",")]
data_list = list(set(data_list))
result = []
for i in range(len(data_list)):
    for j in range(i + 1, len(data_list)):
        result.append(
            f"ts_regression(ts_zscore({data_list[i]}, 500), ts_zscore({data_list[j]}, 500), 500)"
        )
print(len(result))
for i in result:
    print(i)
