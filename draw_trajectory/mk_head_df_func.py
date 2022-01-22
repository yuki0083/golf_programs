import pandas as pd
import utils


def mk_head_df(detected_df_csv_path):
    df = utils.read_csv_to_df(detected_df_csv_path)
    head_df = df[(df["class"]==1)]
    return head_df

def main():
    detected_df_csv_path = "runs/detect/exp/detected_df.csv"
    df = mk_head_df(detected_df_csv_path)

if __name__ == "__main__":
    main()