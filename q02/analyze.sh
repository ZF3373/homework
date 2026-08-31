#!/usr/bin/env bash
# 用法: ./analyze.sh <csv文件路径>
# 功能: 统计 HTTP 5xx 次数最多的前 2 个 path；输出平均 latency_ms（两位小数）

if [ $# -ne 1 ]; then
    echo "Usage: $0 <csv文件路径>" >&2
    exit 1
fi

CSV="$1"
if [ ! -f "$CSV" ]; then
    echo "错误：文件 $CSV 不存在" >&2
    exit 2
fi

# 5xx 计数：跳过表头（NR>1），status>=500 按 path 计数；
# 按次数降序、次数相同按 path 字典序排序，取前 2
awk -F',' 'NR>1 && $4 >= 500 { cnt[$3]++ }
    END { for (p in cnt) print cnt[p], p }' "$CSV" \
    | sort -k1nr -k2 \
    | head -n 2

# 全部数据行平均 latency_ms：跳过表头，保留两位小数
awk -F',' 'NR>1 { sum+=$5; num++ }
    END { printf "%.2f\n", sum/num }' "$CSV"
