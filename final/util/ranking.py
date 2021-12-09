'''quick sort'''
def sort_by_ranking(biz):
    if biz == []:
        return []
    else:
        piv = biz[0]
        part_1 = sort_by_ranking([x for x in biz[1:] if x['rating'] >= piv['rating']])
        part_2 = sort_by_ranking([x for x in biz[1:] if x['rating'] <  piv['rating']])
        return part_1 + [piv] + part_2

'''types of restaurant/food based on weather brackets'''
def sort_by_weather(temp, weather, biz):
    final = []
    if temp >= 70:
        for x in biz:
            for y in x['categories']:
                if "icecream" in y['alias']:
                    if x not in final:
                        final.append(x)
                elif 'desserts' in y['alias']:
                    if x not in final:
                        final.append(x)
                elif 'bars' in y['alias']:
                    if x not in final:
                        final.append(x)
                elif "markets" in y['alias']:
                    if x not in final:
                        final.append(x)
        if final == []:
            for x in biz:
                final.append(x)
    elif temp < 70 and temp >= 50:
        if weather == "Clear":
            for x in biz:
                for y in x['categories']:
                    if 'foodtrucks' in y['alias']:
                        if x not in final:
                            final.append(x)
                        elif 'streetvendors' in y['alias']:
                            if x not in final:
                                final.append(x)
                        elif 'acaibowls' in y['alias']:
                            if x not in final:
                                final.append(x)
        else:
            for x in biz:
                for y in x['categories']:
                    if 'poke' in y['alias']:
                        if x not in final:
                            final.append(x)
                        elif 'bakeries' in y['alias']:
                            if x not in final:
                                final.append(x)
                        elif 'sushi' in y['alias']:
                            if x not in final:
                                final.append(x)
            if final == []:
                for x in biz:
                    final.append(x)
    elif temp < 50 and temp >= 30:
        for x in biz:
            for y in x['categories']:
                if "chinese" in y['alias']:
                    if x not in final:
                        final.append(x)
                elif 'asianfusion' in y['alias']:
                    if x not in final:
                        final.append(x)
                elif "noodles" in y['alias']:
                    if x not in final:
                        final.append(x)
        if final == []:
            for x in biz:
                final.append(x)
    else:
        if weather != "Clear":
            for x in biz:
                if 'delivery' in x['transactions']:
                    if x not in final:
                        final.append(x)
        else:
            for x in biz:
                for y in x['categories']:
                    if "soup" in y['alias']:
                        if x not in final:
                            final.append(x)
                    elif 'hotpot' in y['alias']:
                        if x not in final:
                            final.append(x)
                    elif 'mexican' in y['alias']:
                        if x not in final:
                            final.append(x)
            if final == []:
                for x in biz:
                    final.append(x)
    return final


def sort_by_takeout(temp, forecast, biz):
    final = []
    if temp <= 50 or forecast != "Clear":
        for x in biz:
            if 'delivery' in x['transactions']:
                final.append(x)
            return final
    else:
        for x in biz:
            final.append(x)
        return final
