# build stage
FROM node:16.18-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm set strict-ssl false --global
RUN npm ci --only=production
COPY . .
 
EXPOSE 8094
CMD ["node", "index.js"]
