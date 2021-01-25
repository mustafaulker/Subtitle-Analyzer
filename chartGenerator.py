import matplotlib.pyplot as plt
import pandas as pd


def generate_chart(excel_file, chart_direction):
    data = pd.read_excel(f'./{excel_file}.xlsx')
    if chart_direction == "Horizontal":
        top_10 = data.head(100)
        plt.figure(figsize=(20, 8))
        x = range(100)
        plt.bar(x, top_10['Count'])
        plt.xticks(x, top_10['Word'], rotation='vertical')
        plt.xlabel('Words')
        plt.ylabel('Counts')
        plt.savefig('horizontal-Chart.png')
        print("Horizontal chart saved.")

    elif chart_direction == "Vertical":
        top_10 = data.head(100)
        plt.figure(figsize=(8, 20))
        plt.barh(top_10['Word'], top_10['Count'])
        plt.title("Word-Count Char of IMDB Top100 movie's subtitles.\n Only the top100 word addressed.")
        plt.ylabel('Words')
        plt.xlabel('Count')
        plt.savefig('vertical-Chart.png')
        print("Vertical chart saved.")

    else:
        print("Something went wrong. Check your file or direction input.")
