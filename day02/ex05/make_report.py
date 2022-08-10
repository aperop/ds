import sys
from config import *
from analytics import Research


if __name__ == '__main__':
    if len(sys.argv) == 2:
        r = Research(sys.argv[1])
        fr = r.file_reader()
        count = r.Calculations(fr).counts()
        percent = r.Calculations(fr).fractions(count)
        rand_obs = r.Analytics(fr).predict_random(num_of_steps)
        data = template.format(
                    sum(count),
                    count[0],
                    count[1],
                    percent[0],
                    percent[1],
                    num_of_steps,
                    list(map(sum, zip(*rand_obs)))[0],
                    list(map(sum, zip(*rand_obs)))[1]
                    )
        r.Analytics.save_file(data, name_of_file, type_of_file)
    else:
        print("Use: python3.10 make_report.py data.csv")