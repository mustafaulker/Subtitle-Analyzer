import matplotlib.pyplot as plt
import pandas as pd


# Generate chart with the data in excel file.
def generate_chart(excel_file, chart_direction):
    data = pd.read_excel(f'./data_output/{excel_file}.xlsx')    # Read excel file
    top_100 = data.head(100)  # Get top 100 words and their counts

    if chart_direction == "Horizontal":
        plt.figure(figsize=(30, 12))    # Figure size
        plt.bar(range(100), top_100['Count'])   # Create bars
        plt.xticks(range(100), top_100['Word'], rotation='vertical')    # Labels of bars

        # Chart & axis naming
        plt.title("Word-Count Chart of IMDB Top100 movie's subtitles.\n Only the top100 words addressed.")
        plt.xlabel('Words')
        plt.ylabel('Counts')

        # Write the exact value of the bar, on the top of the bar.
        for index, data in enumerate(top_100['Count']):
            plt.text(x=index, y=data + 1, s=f"{data}", fontdict=dict(fontsize=7), ha="center")

        plt.savefig('./data_output/horizontal-Chart.png')   # Save figure to folder.

    # Same code but 'plt.barh' (horizontal bar)
    elif chart_direction == "Vertical":
        plt.figure(figsize=(12, 30))
        plt.barh(top_100['Word'], top_100['Count'])
        plt.title("Word-Count Chart of IMDB Top100 movie's subtitles.\n Only the top100 words addressed.")
        plt.ylabel('Words')
        plt.xlabel('Count')

        for index, data in enumerate(top_100['Count']):
            plt.text(x=data + 18, y=index, s=f"{data}", fontdict=dict(fontsize=7), va="center")

        plt.savefig('./data_output/vertical-Chart.png')
    else:
        print("Something went wrong. Check excel file or direction input.")

    print(f'{chart_direction} chart saved in the "data_output" folder.')
