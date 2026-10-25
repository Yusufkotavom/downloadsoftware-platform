# Stage 1: Build static assets
FROM node:20-alpine AS builder
RUN corepack enable && corepack prepare pnpm@9 --activate
WORKDIR /app

COPY package.json pnpm-lock.yaml* ./
RUN pnpm install --no-frozen-lockfile

COPY . .
ENV ASTRO_TELEMETRY_DISABLED=1
RUN pnpm run build

# Stage 2: Serve with lightweight Caddy
FROM caddy:2-alpine
COPY --from=builder /app/dist /usr/share/caddy
EXPOSE 80
CMD ["caddy", "file-server", "--root", "/usr/share/caddy", "--listen", ":80"]
