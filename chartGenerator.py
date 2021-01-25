import matplotlib.pyplot as plt
import pandas as pd


def generate_chart(excel_file, chart_direction):
    data = pd.read_excel(f'./data_output/{excel_file}.xlsx')
    if chart_direction == "Horizontal":
        top_100 = data.head(100)
        plt.figure(figsize=(30, 12))
        x = range(100)
        plt.bar(x, top_100['Count'])
        plt.xticks(x, top_100['Word'], rotation='vertical')
        plt.xlabel('Words')
        plt.ylabel('Counts')

        for index, data in enumerate(top_100['Count']):
            plt.text(x=index, y=data + 1, s=f"{data}", fontdict=dict(fontsize=7), ha="center")

        plt.savefig('./data_output/horizontal-Chart.png')
        print("Horizontal chart saved in data_output folder.")

    elif chart_direction == "Vertical":
        top_100 = data.head(100)
        plt.figure(figsize=(12, 30))
        plt.barh(top_100['Word'], top_100['Count'])
        plt.title("Word-Count Char of IMDB Top100 movie's subtitles.\n Only the top100 word addressed.")
        plt.ylabel('Words')
        plt.xlabel('Count')

        for index, data in enumerate(top_100['Count']):
            plt.text(x=data + 18, y=index, s=f"{data}", fontdict=dict(fontsize=7), va="center")

        plt.savefig('./data_output/vertical-Chart.png')
        print("Vertical chart saved in data_output folder.")

    else:
        print("Something went wrong. Check your file or direction input.")
