def gen_core_imp_def_dict(pl, desc=dict()):

def gen_core_json_patch(filename, pl, desc):
    res = gen_core_imp_def_dict(pl, desc)
    import json
    lines = json.dumps(res, indent=4).split("\n")
    return f"""
diff --git a/{filename} b/{filename}
new file mode 100644
--- /dev/null
+++ b/{filename}
@@ -0,0 +1,{len(lines)} @@
{"\n".join(map(lambda x: f"+{x}", lines))}
""".strip()

    json.dump(res, sys.stdout, indent=4)