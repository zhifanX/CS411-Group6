def sort_by_ranking(biz): '''quick sort'''
    if biz == []:
        return []
    else:
        piv = biz[0]
        part_1 = sort_by_ranking([x for x in biz[1:] if x['rating'] >= piv['rating']])
        part_2 = sort_by_ranking([x for x in biz[1:] if x['rating'] <  piv['rating']])
        return part_1 + [piv] + part_2

def sort_by_weather(weather, biz): '''types of restaurant/food based on weather brackets'''
    final = []
    if weather >= 70:
        for x in biz:
            if "icecream" in x['categories']:
                if x not in final:
                    final.append(x)
            elif "markets" in x['categories']:
                if x not in final:
                    final.append(x)
    elif weather < 70 && weather >= 50: '''standard range with all foods'''
        if 'restaurants' in x['categories']:
            if x no in final:
                final.append(x)
    elif weather < 50 && weather >= 30:
        for x in biz:
            if 'panasian' in x['categories']:
                if x not in final:
                    final.append(x)
            elif 'asianfusion' in x['categories']:
                if x not in final:
                    final.append(x)
    else:
        for x in biz:
            if 'soup' in x['categories']:
                if x not in final:
                    final.append(x)
            elif 'hotpot' in x['categories']:
                if x not in finaal:
                    final.append(x)
    return final



def sort_by_takeout(weather, biz): '''give restaurants with takeout option'''
    final = []
    if weather <= 50:
        for x in biz:
            print(x['transactions'])
            if 'delivery' in x['transactions']:
                final.append(x)
            return final
    else:
        for fix x in biz:
            final.append(x)
        return final


'''
Cut off extra restaurants - give limit
'''
