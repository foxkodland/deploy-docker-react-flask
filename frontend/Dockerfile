# FROM node:alpine as build

# COPY package.json package.json
# RUN npm install
# COPY . .
# RUN npm run build

FROM nginx:stable-alpine

# COPY --from=build /dist /usr/share/nginx/html
COPY . /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 6052
CMD [ "nginx", "-g", "daemon off;" ]