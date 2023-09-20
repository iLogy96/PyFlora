import pandas as pd
import matplotlib.pyplot as plt

def create_dataframe_from_data(data_objects):
    """
    Creates a pandas DataFrame from a list of Data objects.

    Parameters:
    data_objects (list): A list of Data objects.

    Returns:
    pd.DataFrame: The pandas DataFrame containing the data from the Data objects.
    """
    new_dict = {
        "TEMP": [d.sen_temp for d in data_objects],
        "HYDRATION": [d.sen_hydration for d in data_objects],
        "PH": [d.sen_pH for d in data_objects],
        "TIME": [d.sen_date for d in data_objects],
    }

    df = pd.DataFrame(new_dict)
    df["TIME"] = pd.to_datetime(df["TIME"]).dt.strftime('%d.%m.%Y. %H:%M:%S')
    return df

def plot_graph(df, plot_type='line'):
    """
    Plots graphs based on the pandas DataFrame created from Data objects.

    Parameters:
    df (pd.DataFrame): The pandas DataFrame containing the data to be plotted.
    plot_type (str): The type of plot to be displayed (bar, pie, line).
    """
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(8, 12))
    color_map = {'TEMP': 'green', 'HYDRATION': 'blue', 'PH': 'red'}

    if plot_type == 'pie':
        for i, column in enumerate(['TEMP', 'HYDRATION', 'PH']):
            if df[column].min() >= 0:
                df[-10:].plot(kind=plot_type, y=column, title=column, autopct='%1.1f%%', legend=False, ax=axes[i])
            else:
                axes[i].text(0.5, 0.5, "Pie plot doesn't allow negative values", ha='center', va='center', transform=axes[i].transAxes)
            axes[i].set_ylabel('')

    else:
        for i, column in enumerate(['TEMP', 'HYDRATION', 'PH']):
            df[-10:].plot(kind=plot_type, x='TIME', y=column, color=color_map[column], ax=axes[i], legend=False)
            axes[i].set_title(column)

    plt.tight_layout()
    plt.show()
