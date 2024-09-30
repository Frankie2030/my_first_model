FROM ubuntu:22.04

# Install system dependencies for conda and python
RUN apt-get update && \
    apt-get install -y wget bzip2 && \
    apt-get clean

# Install Miniconda (lightweight version of Anaconda)
FROM continuumio/miniconda3

# Update PATH to include conda
ENV PATH="/opt/conda/envs/kncn/bin:$PATH"

# Create a new conda environment using environment.yml (make sure you copy the environment.yml file)
WORKDIR /app
COPY environment.yml .

# Install conda environment from the environment.yml file
RUN conda install mamba -n base -c conda-forge
RUN mamba env create -f environment.yml

# Activate the environment in the Docker image
SHELL ["conda", "run", "-n", "kncn", "/bin/bash", "-c"]

# Set the environment to be activated by default
RUN echo "conda activate kncn" >> ~/.bashrc

# Copy the rest of the application code
ADD ./backend /app/backend
ADD ./docker /app/docker
ADD ./research /app/research

# Make sure necessary directories are created
RUN mkdir -p /app/backend/server/static

# Install gunicorn using conda
RUN mamba install -n kncn gunicorn=22.0.0

RUN chmod +x /app/docker/backend/wsgi-entrypoint.sh

# Set the default command to activate the conda environment
CMD ["conda", "run", "-n", "kncn", "gunicorn", "-b", "0.0.0.0:8000", "backend.wsgi"]
