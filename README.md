# **Titanic Analysis Pipeline using Docker**

### **Project Overview**
The project implements a data analysis pipeline to analyze the Titanic dataset. It includes several Python scripts for data preprocessing, exploratory data analysis (EDA), visualization, and modeling, and the pipeline is executed within a Docker container to ensure consistency and reproducibility.

### **Docker file Commands**

- `FROM ubuntu`
    Specifies ubuntu base image for the Docker container.

- `RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*`

    Updates the package lists and installs necessary packages.

- `RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy`

    Installs required Python packages using `pip3`.

- `RUN mkdir -p /home/doc-bd-a1`

    Creates a directory named `doc-bd-a1` inside the container at `/home`.

- `COPY train_titanic.csv /home/doc-bd-a1/`

    Copies titanic dataset file `train_titanic.csv` from the local machine to the container's `/home/doc-bd-a1/` directory.

- `COPY load.py /home/doc-bd-a1/`
- `COPY dpre.py /home/doc-bd-a1/`
- `COPY eda.py /home/doc-bd-a1/`
- `COPY model.py /home/doc-bd-a1/`
- `COPY vis.py /home/doc-bd-a1/`

    Copies the Python script files (`load.py`, `dpre.py`, `eda.py`, `model.py`, `vis.py`) from the local machine to the container's `/home/doc-bd-a1/` directory.

- `WORKDIR /home/doc-bd-a1`

    Sets the working directory inside the container to `/home/doc-bd-a1`.

- `CMD ["/bin/bash"]`

    Specifies the bash shell to run when the container starts.

### **Project Excecution**

1) First load the dataset using `load.py`.
2) Calling `dpre.py` to make the preprocessing.
    - Replace null values with  mean of the Age column.
    - Replace null values with mode of the Embarked column.
    - Data normalization.
    - Remove useless  columns.
3) Calling `eda.py` to make the exploratory data analysis (EDA) step.
4) Calling `vis.py` to create the visualization.
5) Calling `model.py` to implement K-means algorithm.
6) Save result and save it on local machine using `final.sh` bash script.

### **Github Repo**
https://github.com/aabdoo23/bd-a1

### **Meet the team**
##### - *Abdelrahman Saleh* 
##### - *Mohamed Abdelfattah*
##### - *Ahmed Sherif*
##### - *Ahmed Kamal*