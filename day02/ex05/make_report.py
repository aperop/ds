import sys
from config import *
from analytics import Research


if __name__ == '__main__':
    if len(sys.argv) == 2:
        r = Research(sys.argv[1])
        fr = r.file_reader()
        count = r.Calculations(fr).counts()
        percent = r.Calculations(fr).fractions(count)
        rand_obs = r.Analytics(fr).predict_random(3)
        with open(name_of_file + '.' + type_of_file, 'w') as f_out:
            f_out.write(template.format(
                sum(count),
                count[0],
                count[1],
                percent[0],
                percent[1],
                num_of_steps,
                rand_obs[0],
                rand_obs[1]
                ))