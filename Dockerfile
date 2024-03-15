FROM ubuntu

# Update package lists and install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install required Python packages
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1

RUN mkdir -p /home/doc-bd-a1/results

#Copy the dataset file to the container
COPY train_titanic.csv /home/doc-bd-a1/

COPY load.py /home/doc-bd-a1/
COPY dpre.py /home/doc-bd-a1/
COPY eda.py /home/doc-bd-a1/
COPY model.py /home/doc-bd-a1/
COPY vis.py /home/doc-bd-a1/


# Set the working directory
WORKDIR /home/doc-bd-a1

# Copy the current directory contents into the container at /app
#COPY . .

CMD ["/bin/bash"]
