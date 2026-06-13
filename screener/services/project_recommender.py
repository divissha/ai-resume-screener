def recommend_projects(missing):

    projects = []

    if "docker" in missing:
        projects.append(
            "Build and deploy a Dockerized Django application"
        )

    if "aws" in missing:
        projects.append(
            "Deploy a portfolio project on AWS EC2"
        )

    if "postgresql" in missing:
        projects.append(
            "Create a PostgreSQL CRUD management system"
        )

    if "machine learning" in missing:
        projects.append(
            "Develop a Machine Learning prediction project"
        )

    if "react" in missing:
        projects.append(
            "Build a React dashboard with API integration"
        )

    return projects