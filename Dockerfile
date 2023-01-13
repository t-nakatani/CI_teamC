FROM python:3.9

# Rust compiler
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

COPY requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /work

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:9090" ]