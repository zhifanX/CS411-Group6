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
def sort_by_weather(weather, biz):
    final = []
    if weather >= 70:
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
    elif weather < 70 and weather >= 50:
        for x in biz:
            for y in x['categories']:
                if 'foodtrucks' in y['alias']:
                    if x not in final:
                        final.append(x)
                    elif 'poke' in y['alias']:
                        if x not in final:
                            final.append(x)
    elif weather < 50 and weather >= 30:
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
    else:
        for x in biz:
            for y in x['categories']:
                if "soup" in y['alias']:
                    if x not in final:
                        final.append(x)
                elif 'hotpot' in y['alias']:
                    if x not in final:
                        final.append(x)
    return final


def sort_by_takeout(weather, biz):
    final = []
    if weather <= 50:
        for x in biz:
            print(x['transactions'])
            if 'delivery' in x['transactions']:
                final.append(x)
            return final
    else:
        for x in biz:
            final.append(x)
        return final
