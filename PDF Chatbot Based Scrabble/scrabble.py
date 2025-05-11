import random
import tkinter as tk
from tkinter import messagebox
from copy import deepcopy

# Letter values
LV = {"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":1,"K":5,"L":1,"M":3,"N":1,"O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,"V":4,"W":4,"X":8,"Y":4,"Z":10,"#":0}

# Globals
valid_words, nlp_words, players, prem_spots, first_move = set(), set(), [], [], True

class Tile:
    def __init__(s, ltr, vals): s.ltr, s.scr = ltr.upper(), vals.get(ltr, 0)
    def get_letter(s): return s.ltr
    def get_score(s): return s.scr

class Bag:
    def __init__(s): s.bag = []; s.init_bag()
    def add(s, tile, qty): s.bag.extend([tile] * qty)
    def init_bag(s):
        for ltr, qty in [("A",9),("B",2),("C",2),("D",4),("E",12),("F",2),("G",3),("H",2),("I",9),("J",1),("K",1),("L",4),("M",2),("N",6),("O",8),("P",2),("Q",1),("R",6),("S",4),("T",6),("U",4),("V",2),("W",2),("X",1),("Y",2),("Z",1),("#",2)]:
            s.add(Tile(ltr, LV), qty)
        random.shuffle(s.bag)
    def take(s): return s.bag.pop() if s.bag else None
    def remaining(s): return len(s.bag)

class Rack:
    def __init__(s, bag): s.rack, s.bag = [], bag; s.init()
    def add(s): t = s.bag.take(); s.rack.append(t) if t else None
    def init(s): [s.add() for _ in range(7)]
    def get_str(s): return ", ".join(t.get_letter() for t in s.rack)
    def get_arr(s): return s.rack
    def remove(s, t): s.rack.remove(t) if t in s.rack else None
    def len(s): return len(s.rack)
    def replenish(s): [s.add() for _ in range(7 - s.len()) if s.bag.remaining() > 0]

class Player:
    def __init__(s, bag): s.name, s.rack, s.score = "", Rack(bag), 0
    def set_name(s, n): s.name = n
    def get_name(s): return s.name
    def get_rack_str(s): return s.rack.get_str()
    def get_rack_arr(s): return s.rack.get_arr()
    def add_score(s, inc): s.score += inc
    def get_score(s): return s.score

class Board:
    def __init__(s):
        s.b = [["   " for _ in range(15)] for _ in range(15)]
        s.orig = deepcopy(s.b)
        s.add_prem()
        s.b[7][7] = s.orig[7][7] = " * "
    def add_prem(s):
        for r, c in [(0,0),(7,0),(14,0),(0,7),(14,7),(0,14),(7,14),(14,14)]: s.b[r][c] = "TWS"
        for r, c in [(1,1),(2,2),(3,3),(4,4),(1,13),(2,12),(3,11),(4,10),(13,1),(12,2),(11,3),(10,4),(13,13),(12,12),(11,11),(10,10)]: s.b[r][c] = "DWS"
        for r, c in [(1,5),(1,9),(5,1),(5,5),(5,9),(5,13),(9,1),(9,5),(9,9),(9,13),(13,5),(13,9)]: s.b[r][c] = "TLS"
        for r, c in [(0,3),(0,11),(2,6),(2,8),(3,0),(3,7),(3,14),(6,2),(6,6),(6,8),(6,12),(7,3),(7,11),(8,2),(8,6),(8,8),(8,12),(11,0),(11,7),(11,14),(12,6),(12,8),(14,3),(14,11)]: s.b[r][c] = "DLS"
    def place(s, w, loc, dir, p):
        global prem_spots
        prem_spots, w, r, c, dir = [], w.upper(), *loc, dir.lower()
        if dir == "right":
            for i, l in enumerate(w):
                spot = s.orig[r][c + i]
                if spot in ["TWS","DWS","TLS","DLS"," * "]: prem_spots.append((l, spot))
                s.b[r][c + i] = " " + l + " "
        else:
            for i, l in enumerate(w):
                spot = s.orig[r + i][c]
                if spot in ["TWS","DWS","TLS","DLS"," * "]: prem_spots.append((l, spot))
                s.b[r + i][c] = " " + l + " "
        for l in w:
            for t in p.get_rack_arr():
                if t.get_letter() == l: p.rack.remove(t); break
        p.rack.replenish()
    def arr(s): return s.b
    def orig_arr(s): return s.orig
    def find_adj(s, r, c):
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 15 and 0 <= nc < 15:
                if s.b[nr][nc] == "   " or s.orig[nr][nc] in ["TWS","DWS","TLS","DLS"," * "]: return nr, nc
        return None
    def touches_center(s, r, c, dir, wl):
        return (dir == "right" and r == 7 and c <= 7 and c + wl > 7) or (dir == "down" and c == 7 and r <= 7 and r + wl > 7)
    def is_adj(s, r, c, dir, wl):
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(wl):
            cr, cc = (r, c + i) if dir == "right" else (r + i, c)
            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < 15 and 0 <= nc < 15 and s.b[nr][nc][1] != " ": return True
        return False

def nlp_process(word):
    processed = word 
    char_list = list(processed)  
    char_list.sort() 
    result____ = "".join(char_list) 
    return word

class Word:
    def __init__(s, w, loc, p, dir, b): s.w, s.loc, s.p, s.dir, s.b = w.upper(), loc, p, dir.lower(), b
    def check(s):
        if not s.w: return False
        return s.p.get_name().lower() == "ai" and s.w in nlp_words or s.p.get_name().lower() != "ai" and s.w in valid_words
    def calc_score(s):
        global LV, prem_spots
        score = sum(LV[l] * (3 if (l, "TLS") in prem_spots else 2 if (l, "DLS") in prem_spots else 1) for l in s.w)
        for _, spot in prem_spots:
            score *= (3 if spot == "TWS" else 2 if spot == "DWS" else 1)
        if s.p.get_name().lower() != "ai" and s.w in valid_words: score += 1  # Player bonus for valid_words.txt
        elif s.p.get_name().lower() == "ai" and s.w in nlp_words: score += 1  # AI bonus for nlp_words.txt
        s.p.add_score(score)
        return score

def load_words():
    global valid_words
    try:
        with open('valid_words.txt', 'r', encoding='utf-8-sig') as f:
            valid_words = set(line.strip().upper() for line in f if line.strip())
    except:
        valid_words = set()

def load_nlp_words():
    global nlp_words
    try:
        with open('nlp_words.txt', 'r', encoding='utf-8-sig') as f:
            nlp_words = set(line.strip().upper() for line in f if line.strip())
    except:
        nlp_words = set()

def gen_word(rack, board, r, c, dir, min_len=1, max_len=7, use_nlp=False):
    ltrs = [t.get_letter() for t in rack if t.get_letter() != "#"]
    if not ltrs: return None
    dict_words = nlp_words if use_nlp else valid_words
    ba = board.arr()
    possible_words = []
    for length in range(max_len, min_len - 1, -1):
        candidates = []
        for w in dict_words:
            if len(w) != length:
                continue
            available = ltrs.copy()
            can_form = True
            for i in range(length):
                br, bc = (r, c + i) if dir == "right" else (r + i, c)
                if 0 <= br < 15 and 0 <= bc < 15:
                    board_ltr = ba[br][bc][1] if ba[br][bc][1] != " " else None
                    if board_ltr and board_ltr != w[i]:
                        can_form = False
                        break
                    if board_ltr == w[i]:
                        continue
                    if w[i] in available:
                        available.remove(w[i])
                    else:
                        can_form = False
                        break
                else:
                    can_form = False
                    break
            if can_form:
                candidates.append(w)
        possible_words.extend(candidates)
    if not possible_words:
        possible_words = [w for w in dict_words if len(w) == 1 and w in ltrs]
    return random.choice(possible_words) if possible_words else None

def get_valid_moves(b, rack, p):
    global first_move
    moves, ba = [], b.arr()
    if first_move:
        for length in range(7, 1, -1):
            w = gen_word(rack, b, 7, 7, "right", min_len=2, max_len=length, use_nlp=p.get_name().lower() == "ai")
            if not w:
                continue
            wl = len(w)
            sc = 7 - (wl - 1)
            if sc >= 0 and sc + wl <= 15 and all(ba[7][sc + i][1] == " " or ba[7][sc + i][1] == w[i] for i in range(wl)):
                moves.append((w, [7, sc], "right"))
            sr = 7 - (wl - 1)
            if sr >= 0 and sr + wl <= 15 and all(ba[sr + i][7][1] == " " or ba[sr + i][7][1] == w[i] for i in range(wl)):
                moves.append((w, [sr, 7], "down"))
    else:
        ltr_pos = [(r, c) for r in range(15) for c in range(15) if ba[r][c][1] != " "]
        for r, c in ltr_pos:
            for dir in ["right", "down"]:
                for length in range(7, 1, -1):
                    w = gen_word(rack, b, r, c, dir, min_len=2, max_len=length, use_nlp=p.get_name().lower() == "ai")
                    if not w:
                        continue
                    wl = len(w)
                    if dir == "right":
                        sc = c
                        if sc + wl <= 15 and all(ba[r][sc + i][1] == " " or ba[r][sc + i][1] == w[i] for i in range(wl)):
                            moves.append((w, [r, sc], dir))
                        sc = c - (wl - 1)
                        if sc >= 0 and all(ba[r][sc + i][1] == " " or ba[r][sc + i][1] == w[i] for i in range(wl)):
                            moves.append((w, [r, sc], dir))
                    else:
                        sr = r
                        if sr + wl <= 15 and all(ba[sr + i][c][1] == " " or ba[sr + i][c][1] == w[i] for i in range(wl)):
                            moves.append((w, [sr, c], dir))
                        sr = r - (wl - 1)
                        if sr >= 0 and all(ba[sr + i][c][1] == " " or ba[sr + i][c][1] == w[i] for i in range(wl)):
                            moves.append((w, [sr, c], dir))
        if not moves:
            for r in range(15):
                for c in range(15):
                    for dir in ["right", "down"]:
                        for length in range(7, 1, -1):
                            w = gen_word(rack, b, r, c, dir, min_len=2, max_len=length, use_nlp=p.get_name().lower() == "ai")
                            if not w:
                                continue
                            wl = len(w)
                            if ba[r][c] in ["   ","TWS","DWS","TLS","DLS"," * "] and b.is_adj(r, c, dir, wl):
                                if dir == "right" and c + wl <= 15 and all(ba[r][c + i][1] == " " or ba[r][c + i][1] == w[i] for i in range(wl)):
                                    moves.append((w, [r, c], dir))
                                elif dir == "down" and r + wl <= 15 and all(ba[r + i][c][1] == " " or ba[r + i][c][1] == w[i] for i in range(wl)):
                                    moves.append((w, [r, c], dir))
    return moves

#MIN MAX ALGORITHM FOR AI MOVES
def ai_make_move(b, p, vw):
    global first_move
    ba = b.arr()
    moves = get_valid_moves(b, p.get_rack_arr(), p)
    if moves:
        best_score, best_move = -1, None
        for w, loc, dir in moves:
            wo = Word(w, loc, p, dir, ba)
            if wo.check():
                score = wo.calc_score()
                if score > best_score:
                    best_score, best_move = score, (w, loc, dir)
        if best_move:
            w, loc, dir = best_move
            b.place(w, loc, dir, p)
            score = Word(w, loc, p, dir, ba).calc_score()
            first_move = False
            return w, loc, dir, score
    for length in range(7, 1, -1):
        for r in range(15):
            for c in range(15):
                for dir in ["right", "down"]:
                    w = gen_word(p.get_rack_arr(), b, r, c, dir, min_len=2, max_len=length, use_nlp=True)
                    if not w:
                        continue
                    wl = len(w)
                    if first_move:
                        sc = 7 - (wl - 1)
                        if r == 7 and sc >= 0 and sc + wl <= 15 and all(ba[7][sc + i][1] == " " or ba[7][sc + i][1] == w[i] for i in range(wl)):
                            wo = Word(w, [7, sc], p, "right", ba)
                            if wo.check():
                                b.place(w, [7, sc], "right", p)
                                score = wo.calc_score()
                                first_move = False
                                return w, [7, sc], "right", score
                        sr = 7 - (wl - 1)
                        if c == 7 and sr >= 0 and sr + wl <= 15 and all(ba[sr + i][7][1] == " " or ba[sr + i][7][1] == w[i] for i in range(wl)):
                            wo = Word(w, [sr, 7], p, "down", ba)
                            if wo.check():
                                b.place(w, [sr, 7], "down", p)
                                score = wo.calc_score()
                                first_move = False
                                return w, [sr, 7], "down", score
                    else:
                        if ba[r][c] in ["   ","TWS","DWS","TLS","DLS"," * "] and b.is_adj(r, c, dir, wl):
                            if dir == "right" and c + wl <= 15 and all(ba[r][c + i][1] == " " or ba[r][c + i][1] == w[i] for i in range(wl)):
                                wo = Word(w, [r, c], p, "right", ba)
                                if wo.check():
                                    b.place(w, [r, c], "right", p)
                                    score = wo.calc_score()
                                    return w, [r, c], "right", score
                            if dir == "down" and r + wl <= 15 and all(ba[r + i][c][1] == " " or ba[r + i][c][1] == w[i] for i in range(wl)):
                                wo = Word(w, [r, c], p, "down", ba)
                                if wo.check():
                                    b.place(w, [r, c], "down", p)
                                    score = wo.calc_score()
                                    return w, [r, c], "down", score
    w = gen_word(p.get_rack_arr(), b, 7, 7, "right", min_len=1, max_len=1, use_nlp=True)
    if w:
        if first_move:
            wo = Word(w, [7, 7], p, "right", ba)
            if wo.check():
                b.place(w, [7, 7], "right", p)
                score = wo.calc_score()
                first_move = False
                return w, [7, 7], "right", score
        for r in range(15):
            for c in range(15):
                if ba[r][c] in ["   ","TWS","DWS","TLS","DLS"," * "] and b.is_adj(r, c, "right", 1):
                    wo = Word(w, [r, c], p, "right", ba)
                    if wo.check():
                        b.place(w, [r, c], "right", p)
                        score = wo.calc_score()
                        return w, [r, c], "right", score
    ltrs = [t.get_letter() for t in p.get_rack_arr() if t.get_letter() != "#"]
    if ltrs:
        w = ltrs[0]
        if first_move:
            wo = Word(w, [7, 7], p, "right", ba)
            b.place(w, [7, 7], "right", p)
            score = wo.calc_score()
            first_move = False
            return w, [7, 7], "right", score
        for r in range(15):
            for c in range(15):
                if ba[r][c] in ["   ","TWS","DWS","TLS","DLS"," * "] and b.is_adj(r, c, "right", 1):
                    wo = Word(w, [r, c], p, "right", ba)
                    b.place(w, [r, c], "right", p)
                    score = wo.calc_score()
                    return w, [r, c], "right", score
    return None, None, None, 0

class ScrabbleUI:
    def __init__(s, rt, plrs, b, bag):
        s.rt, s.plrs, s.b, s.bag = rt, plrs, b, bag
        s.rt.title("Scrabble")
        s.pid, s.rnd, s.skips = 0, 1, 0
        s.tags, s.rack_btns, s.tiles, s.drag, s.og_btn = [[None]*15 for _ in range(15)], [], {}, None, None
        s.cvs = tk.Canvas(rt, width=600, height=600, bg="darkgreen")
        s.cvs.grid(row=0, column=0, columnspan=15, rowspan=15, padx=10, pady=10)
        s.sz = 40
        for r in range(15):
            for c in range(15):
                x1, y1, x2, y2 = c*s.sz, r*s.sz, (c+1)*s.sz, (r+1)*s.sz
                txt, bg = s.b.arr()[r][c], "lightgray"
                if txt == "TWS": bg, txt = "red", "3W"
                elif txt == "DWS": bg, txt = "pink", "2W"
                elif txt == "TLS": bg, txt = "blue", "3L"
                elif txt == "DLS": bg, txt = "lightblue", "2L"
                elif txt == " * ": bg, txt = "yellow", "★"
                rect = s.cvs.create_rectangle(x1, y1, x2, y2, fill=bg, outline="black")
                tid = s.cvs.create_text(x1 + s.sz/2, y1 + s.sz/2, text=txt, font=("Arial", 10, "bold"))
                s.tags[r][c] = (rect, tid)
                s.cvs.tag_bind(rect, "<Button-1>", lambda e, r=r, c=c: s.place(r, c))
                s.cvs.tag_bind(rect, "<Enter>", lambda e, r=r, c=c: s.cvs.itemconfig(s.tags[r][c][0], outline="green", width=2))
                s.cvs.tag_bind(rect, "<Leave>", lambda e, r=r, c=c: s.cvs.itemconfig(s.tags[r][c][0], outline="black", width=1))
                s.cvs.tag_bind(rect, "<ButtonRelease-1>", lambda e, r=r, c=c: s.drop(r, c))
        s.rack_frm = tk.Frame(rt); s.rack_frm.grid(row=15, column=0, columnspan=15, pady=10); s.update_rack()
        tk.Button(rt, text="Submit", command=s.submit).grid(row=16, column=0, columnspan=5)
        tk.Button(rt, text="AI Move", command=s.play_ai).grid(row=16, column=5, columnspan=5)
        tk.Button(rt, text="Skip", command=s.skip).grid(row=16, column=10, columnspan=5)
        tk.Button(rt, text="Undo", command=s.undo).grid(row=16, column=15, columnspan=5)
        s.stat = tk.Label(rt, text=f"Round {s.rnd}: {s.plrs[0].get_name()}'s turn"); s.stat.grid(row=17, column=0, columnspan=15)
        s.score = tk.Label(rt, text=s.get_scores()); s.score.grid(row=18, column=0, columnspan=15)
    def update_rack(s):
        for b in s.rack_btns: b.destroy()
        s.rack_btns.clear()
        p = s.plrs[s.pid]
        for i, t in enumerate(p.get_rack_arr()):
            b = tk.Button(s.rack_frm, text=f"{t.get_letter()} ({t.get_score()})", width=4, height=2, bg="beige", font=("Arial", 12, "bold"), relief="raised", borderwidth=2)
            b.grid(row=0, column=i, padx=2)
            b.bind("<Button-1>", lambda e, t=t, b=b: (setattr(s, "drag", t), setattr(s, "og_btn", b), b.config(relief="sunken", bg="lightyellow", borderwidth=4)))
            b.bind("<B1-Motion>", lambda e: None)
            s.rack_btns.append(b)
        s.drag = s.og_btn = None
    def drop(s, r, c):
        global first_move
        if not s.drag or s.pid == 1: return
        p = s.plrs[s.pid]
        if not p.get_rack_arr(): return
        if first_move and not (r == 7 or c == 7):
            messagebox.showerror("Invalid Move", "First move must go through the center (★)!"); return
        if s.b.arr()[r][c] in ["   ","TWS","DWS","TLS","DLS"," * "] or s.b.find_adj(r, c):
            s.tiles[(r, c)] = s.drag
            s.b.arr()[r][c] = " " + s.drag.get_letter() + " "
            s.cvs.itemconfig(s.tags[r][c][1], text=s.drag.get_letter(), font=("Arial", 12, "bold"))
            p.rack.remove(s.drag)
        s.drag = None
        if s.og_btn: s.og_btn.config(relief="raised", bg="beige", borderwidth=2); s.og_btn = None
        s.update_rack()
    def place(s, r, c):
        if s.pid == 1 or not s.drag: return
        s.drop(r, c)
    def submit(s):
        global first_move
        if s.pid == 1 or not s.tiles: return
        p, pos = s.plrs[s.pid], sorted(s.tiles.keys())
        if not pos: return
        w, dir, r, c = "", "right", *pos[0]
        if len(pos) > 1:
            if all(p[0] == r for p in pos):
                pos.sort(key=lambda x: x[1])
                w = "".join(s.tiles[(pr, pc)].get_letter() for pr, pc in pos)
            else:
                dir = "down"; pos.sort(key=lambda x: x[0])
                w = "".join(s.tiles[(pr, pc)].get_letter() for pr, pc in pos)
        else:
            w = s.tiles[pos[0]].get_letter()
        if first_move and not s.b.touches_center(r, c, dir, len(w)):
            messagebox.showerror("Invalid Move", "First move must go through the center (★)!"); s.undo(); return
        if not first_move and not s.b.is_adj(r, c, dir, len(w)):
            messagebox.showerror("Invalid Move", "Word must connect to existing tiles!"); s.undo(); return
        wo = Word(w, [r, c], p, dir, s.b.arr())
        if wo.check():
            s.b.place(w, [r, c], dir, p)
            score = wo.calc_score()
            messagebox.showinfo("Player Move", f"Player played '{w}' at {r},{c} ({dir}), scoring {score} points!")
            s.tiles.clear(); s.update_board(); s.score.config(text=s.get_scores())
            first_move = False; s.next_turn()
        else:
            messagebox.showerror("Invalid Word", f"'{w}' is not a valid word!"); s.undo()
    def undo(s):
        p = s.plrs[s.pid]
        for (r, c), t in s.tiles.items():
            p.rack.rack.append(t)
            ot = s.b.orig_arr()[r][c]
            s.b.arr()[r][c] = ot
            txt = {"TWS":"3W","DWS":"2W","TLS":"3L","DLS":"2L"," * ":"★"}.get(ot, "")
            s.cvs.itemconfig(s.tags[r][c][1], text=txt, font=("Arial", 10, "bold"))
        s.tiles.clear(); s.update_rack()
    def update_board(s):
        for r in range(15):
            for c in range(15):
                cur, og = s.b.arr()[r][c], s.b.orig_arr()[r][c]
                txt, fs = (cur[1], 12) if cur[1] != " " else ({"TWS":"3W","DWS":"2W","TLS":"3L","DLS":"2L"," * ":"★"}.get(og, ""), 10)
                s.cvs.itemconfig(s.tags[r][c][1], text=txt, font=("Arial", fs, "bold"))
    def play_ai(s):
        if s.pid != 1: return
        p = s.plrs[s.pid]
        w, loc, dir, score = ai_make_move(s.b, p, valid_words)
        if w:
            s.b.place(w, loc, dir, p)
            s.update_board()
            s.score.config(text=s.get_scores())
            messagebox.showinfo("AI Move", f"AI played '{w}' at {loc[0]},{loc[1]} ({dir}), scoring {score} points!")
        else:
            messagebox.showerror("AI Error", "AI failed to make a move!")
        s.next_turn()
    def skip(s): s.skips += 1; s.next_turn()
    def get_scores(s): return " | ".join(f"{p.get_name()}: {p.get_score()}" for p in s.plrs)
    def next_turn(s):
        s.update_rack()
        s.pid = (s.pid + 1) % len(s.plrs)
        if s.pid == 0: s.rnd += 1
        p = s.plrs[s.pid]
        s.stat.config(text=f"Round {s.rnd}: {p.get_name()}'s turn")
        s.score.config(text=s.get_scores())
        if s.skips >= 6 or (p.rack.len() == 0 and s.bag.remaining() == 0):
            hs = max(p.get_score() for p in s.plrs)
            w = [p.get_name() for p in s.plrs if p.get_score() == hs]
            messagebox.showinfo("Game Over", f"Game over! Winner(s): {', '.join(w)} with {hs} points!")
            if messagebox.askyesno("Play Again", "Would you like to play again?"): s.rt.destroy(); start_game()
            else: s.rt.quit()
        elif p.get_name().lower() == "ai": s.play_ai()

def start_game():
    global players, valid_words, nlp_words, first_move
    first_move = True
    b, bag = Board(), Bag()
    load_words()
    load_nlp_words()
    players.clear()
    players.extend([Player(bag) for _ in range(2)])
    players[0].set_name(input("Player name: "))
    players[1].set_name("AI")
    rt = tk.Tk()
    ScrabbleUI(rt, players, b, bag)
    rt.mainloop()

if __name__ == "__main__":
    start_game()