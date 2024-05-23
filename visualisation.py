import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visualize_top_starred_projects(df, save_path=None):
    # Top 10 most starred projects
    top_starred = df.nlargest(10, 'stars')


    # Visualize the top 10 most starred projects
    plt.figure(figsize=(10, 6))
    sns.barplot(x='stars', y='name', data=top_starred)
    plt.title('Top 10 Most Starred Projects on GitHub')
    plt.xlabel('Stars')
    plt.ylabel('Repository Name')


    # Save the plot as an image if save_path is provided
    if save_path:
        os.makedirs(save_path, exist_ok=True)
        plt.savefig(os.path.join(save_path, 'top_starred_projects.png'))


    plt.show()


def visualize_language_popularity(df, save_path=None):
    # Language popularity
    language_trends = df['language'].value_counts()


    # Visualize language popularity
    plt.figure(figsize=(14, 7))
    sns.barplot(x=language_trends.values, y=language_trends.index)
    plt.title('Programming Language Popularity on GitHub')
    plt.xlabel('Number of Repositories')
    plt.ylabel('Programming Language')


    # Save the plot as an image if save_path is provided
    if save_path:
        os.makedirs(save_path, exist_ok=True)
        plt.savefig(os.path.join(save_path, 'language_popularity.png'))


    plt.show()


def visualize_top_owners(df, save_path=None):
    # Top owners (users/organizations) with the most repositories
    top_owners = df['owner'].value_counts().nlargest(10)


    # Visualize the top owners
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_owners.values, y=top_owners.index)
    plt.title('Top Owners (Users/Organizations) with Most Repositories on GitHub')
    plt.xlabel('Number of Repositories')
    plt.ylabel('Owner')
    plt.xticks(rotation=45, ha='right')


    # Save the plot as an image if save_path is provided
    if save_path:
        os.makedirs(save_path, exist_ok=True)
        plt.savefig(os.path.join(save_path, 'top_owners.png'))


    plt.show()








def visualize_license_distribution(df, save_path=None):
    # Count the occurrences of each license
    license_counts = df['license'].value_counts()


    # Visualize the license distribution
    plt.figure(figsize=(10, 6))
    license_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Licenses in Top Repositories')
    plt.ylabel('')  # Remove y-label
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle


    # Save the plot as an image if save_path is provided
    if save_path:
        os.makedirs(save_path, exist_ok=True)
        plt.savefig(os.path.join(save_path, 'license_distribution.png'))


    plt.show()






def main():
    # Load the data
    df = pd.read_csv('github_repos.csv')


    # Visualize top starred projects and save the image
    visualize_top_starred_projects(df, save_path='results')


    # Visualize language popularity and save the image
    visualize_language_popularity(df, save_path='results')


    # Visualize top owners and save the image
    visualize_top_owners(df, save_path='results')


    # Visualize license distribution and save the image
    visualize_license_distribution(df, save_path='results')




if __name__ == "__main__":
    main()