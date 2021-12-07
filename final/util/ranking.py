def sort_by_ranking(biz):
    if biz == []:
        return []
    else:
        piv = biz[0]
        part_1 = sort_by_ranking([x for x in biz[1:] if x['rating'] >= piv['rating']])
        part_2 = sort_by_ranking([x for x in biz[1:] if x['rating'] <  piv['rating']])
        return part_1 + [piv] + part_2

def sort_by_weather(weather, biz):
    final = []
    if weather >= 70:
        for x in biz:
            if x['categories'] == "icecream":
                if biz[x] not in final:
                    final.append(biz[x])
                    '''
    if weather >= 50:
        for x in biz:
            if biz[x]['categories'] == '''
    return final



def sort_by_takeout(biz):
    final = []
    for x in biz:
        print(x['transactions'])
        if 'delivery' in x['transactions']:
            final.append(x)
    return final


'''
Cut off extra restaurants - give limit
'''
