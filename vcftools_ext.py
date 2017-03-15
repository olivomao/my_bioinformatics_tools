'''

extension procedures based on usage of vcftools

'''

import sys, pdb

'''
given a file, find histogram statistics (col val, cnt) of a particular column,
output (sorted in pattern/col val) the statistics

usage:

python vcftools_ext.py --col_val_hist
                       --input if_path
                       --col  col_idx (0-based)
                       [--skip_1st_line * default false]
                       [--output of_path * default if_path.col_<col>_val_hist]
'''

def col_val_hist(args):

    if_path = args[args.index('--input')+1]

    col_idx = int(args[args.index('--col')+1])

    if '--skip_1st_line' in args:
        skip = True 
    else:
        skip = False 
    
    if '--output' in args:
        of_path = args[args.index('--output')+1]
    else:
        of_path = if_path + '.col_%d_val_hist'%col_idx

    pdb.set_trace()

    with open(if_path, 'r') as in_f, open(of_path, 'w') as out_f:

        hist_stat = {} #key - col val; val - cnt

        if skip == True:
            in_f.readline()

        for line in in_f:
            col_val = line.split()[col_idx]
            if col_val in hist_stat:
                hist_stat[col_val] += 1
            else:
                hist_stat[col_val] = 1

        itms = hist_stat.items()
        itms.sort(key=lambda x:x[0]) #sort by pattern

        for k, v in itms:
            out_f.write('%s\t%s\n'%(str(k), str(v)))

    print('col_val_hist done')
    print('%s written'%(of_path))

    return

def main():

    return

'''
usage:

# get col hist (pattern - counts)

python vcftools_ext.py --col_val_hist
                       --input if_path
                       --col  col_idx (0-based)
                       [--skip_1st_line * default false]
                       [--output of_path * default if_path.col_<col>_val_hist]
'''

if __name__ == "__main__":

    args = sys.argv

    if '--col_val_hist' in args:
        col_val_hist(args)
    else:
        main()