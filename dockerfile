FROM nginx:alpine

# Install python3, pip3 and poetry
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN apk add --no-cache poetry

# Copy necessary files
COPY pyproject.toml ./
COPY poetry.lock ./
COPY databaseManager ./databaseManager
COPY API ./API
COPY nginx.conf /etc/nginx/nginx.conf
COPY web /usr/share/nginx
COPY startServer.sh /startServer.sh

# Open ports
EXPOSE 80
EXPOSE 8000

# Start command
CMD ["/startServer.sh"]
#CMD ["nginx", "-g", "daemon off;"]
