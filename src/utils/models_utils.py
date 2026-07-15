from sklearn.model_selection import train_test_split


def split_dataset(df,config):
    """
    Split the dataset into training and testing sets.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    tuple
        X_train, X_test, y_train, y_test
    """

    X = df["transformed_text"]

    y = df["label"]

    return train_test_split(
        X,
        y,
        test_size=config.test_size,
        random_state=config.random_state,
        stratify=y if config.stratify else None
    )