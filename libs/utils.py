# enocding: utf-8
'''
Utility functions
'''
import json

# dict整形文字列化
def sprint(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2)

# list 値 or None 取得
def geta(ary, i):
    return ary[i] if i < len(ary) else None
