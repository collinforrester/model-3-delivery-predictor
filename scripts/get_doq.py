import datetime
import argparse


def get_doq(dt):
    return dt.timetuple().tm_yday - \
           datetime.date(dt.year, ((int((dt.month - 1) / 3)) * 3) + 1, 1).timetuple().tm_yday


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--date', type=str, required=True)
    parser.add_argument('-f', '--format', default="%Y-%m-%d")

    args = parser.parse_args()

    if not args.date:
        raise Exception("date required")

    print(get_doq(datetime.datetime.strptime(args.date, args.format)))


if __name__ == "__main__":
    main()
