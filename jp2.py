# inp_lst = [(1, 5), (2, 4), (3, 4), (4, 6), (4, 8), (4, 9), (5, 8), (5, 6)]

def minimum_chairs(inp_lst):
    mns = 0
    end_time_track = {}
    for e_tup in inp_lst:
        st_time, ed_time = e_tup
        gt_time = end_time_track.get(st_time, 0)
        if gt_time == 0:
            mns += 1
            end_time_track[ed_time] = end_time_track.get(ed_time, 0) + 1
        else:
            end_time_track[st_time] = end_time_track.get(st_time, 0) - 1
    return mns
print (minimum_chairs([(1, 5), (2, 4), (3, 4), (4, 6), (4, 8), (4, 9), (5, 8), (5, 6)]))
