# Enterprise-Support-Agent

## 项目简介

Enterprise-Support-Agent 是一个基于 FastAPI 的轻量级智能支持后端服务。它目前提供文档摄取、文本清洗、分块存储和基础 API 接口，方便后续集成检索、向量数据库和检索增强生成（RAG）。

## 主要功能

- FastAPI 服务
  - `/health` 健康检查
  - `/chat` 聊天接口
  - `/ingest` 文档摄取接口
- 本地文档摄取管道
- 文本清洗与规范化
- 支持重叠分块（chunking）
- 文档和分块记录分别存储
- 自动生成 Swagger / OpenAPI 文档

## 当前状态

- ✅ 基础文档摄取与分块功能
- ✅ 本地 JSON 存储
- ✅ FastAPI 接口

## 规划中的功能

- Embeddings 向量生成
- 向量数据库检索
- 检索结果 reranking
- 基于检索证据的真实引用
- 工作流编排与任务管理

## 项目结构

- `app/`
  - `api/` — FastAPI 路由模块
  - `core/` — 配置与日志管理
  - `schemas/` — Pydantic 数据模型
  - `services/` — 业务逻辑服务
  - `storage/` — 本地存储实现
  - `retrieval/` — 文档摄取与分块逻辑
- `data/` — 运行时生成的数据目录
- `README.md` — 项目说明
- `requirements.txt` — Python 依赖

## 快速开始

1. 创建并激活 Python 虚拟环境

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 运行服务

```bash
uvicorn app.main:app --reload
```

4. 打开文档

- Swagger UI: `http://127.0.0.1:8000/docs`
- Redoc: `http://127.0.0.1:8000/redoc`

## API 说明

- `GET /health` — 健康检查
- `POST /ingest` — 上传文档并生成分块
- `POST /chat` — 聊天/问答接口（如已实现）

## 注意事项

- 当前没有向量检索功能，数据仅以本地 JSON 保存。
- 若要扩展检索能力，可考虑集成 OpenAI/Anthropic embeddings 与 Pinecone、Weaviate、Chroma 等向量数据库。

## 贡献

欢迎提交 issue 或 PR，帮助完善摄取、检索、查询和工作流能力。

## day02 2026/05/11 review
- [x] 更新上传文档模组，追加真实pipeline
- [x] 追加清晰文件内容以及分块功能
- [x] 追加文件存储和分块存储功能

## day03 2026/05/12 TODO
- [ ] 让分块从文本块升级成可检索单元
- [ ] 明确元数据内容
- [ ] 为未来retrieval做准备
- [ ] 让chunk具备citation和filter基础
- [ ] 为后边embedidng / vector store接入做好接口