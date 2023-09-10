from testassigment.data import PRICES_FILE_PATH
from testassigment.services import Draw, PlotManager


def run() -> None:
    df = PlotManager.create_df_from_csv_file(PRICES_FILE_PATH)

    df = PlotManager.add_ema(df, 10_000)

    Draw.draw_plot_from_df(df)

    df = PlotManager.format_ohlc(df, "10Min")

    Draw.draw_candles_plot_from_df(df)



if __name__ == "__main__":
    run()


