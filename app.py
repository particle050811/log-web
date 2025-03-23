from flask import Flask, send_file, abort, jsonify
from flask_cors import CORS
import os
import re
import json

app = Flask(__name__)
CORS(app)
contents=["心跳发送成功","BOT_WS链接已断开，正在尝试重连……","BOT_WS链接已因长时间未收到消息而主动断开","BOT_WS链接已断开，正在尝试重连……"]
levels=["WARNING","ERROR"]

@app.route('/logs/<month>/<day>')
def get_logs(month, day):
    if not re.match(r'^\d{1,2}$', month) or not re.match(r'^\d{1,2}$', day):
        abort(400, description="Invalid date format. Use M/D format")

    month = month.zfill(2)
    day = day.zfill(2)
    filepath = f"../xiaoling-bot0830/log/102070552/{month}-{day}.log"

    if not os.path.exists(filepath):
        abort(404, description="Log file not found")

    # 读取并处理日志文件
    log_entries = []
    current_entry = []
    log_pattern = re.compile(r'^\[(\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(INFO|ERROR|WARNING|DEBUG)\] (.*)')

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if log_pattern.match(line):
                if current_entry:
                    log_entries.append('\n'.join(current_entry))
                current_entry = [line]
            else:
                if current_entry:
                    current_entry.append(line)

    if current_entry:
        log_entries.append('\n'.join(current_entry))

    processed_logs = []
    for log in log_entries:
        match = log_pattern.match(log)
        if match:
            content = match.group(3) + ('\n' + '\n'.join(log.split('\n')[1:]) if len(log.split('\n')) > 1 else '')
            level = match.group(2)
            if level in levels:
                continue
            if content in contents:
                continue
            processed_logs.append({
                "timestamp": match.group(1),
                "level": level,
                "content": content
            })
    
    return jsonify({
        "date": f"{month}-{day}",
        "entries": processed_logs,
        "count": len(log_entries)
    })

if __name__ == '__main__':
    os.makedirs('logs', exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)