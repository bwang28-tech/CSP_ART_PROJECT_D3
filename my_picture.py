
import simple_graphics as sg
import random

def draw_point_star(cx, cy, size, color):
    sg.set_fill_color(color)
    sg.set_line_thickness(0)
    sg.set_outline_color("#020210") 
    sg.fill_circle(cx, cy, size)
    
def draw_glow_star(cx, cy, size, color):
    sg.set_line_thickness(0)
    sg.set_outline_color("#020210")
    sg.set_fill_color("black")
    sg.fill_circle(cx, cy, size * 4)
    sg.set_fill_color("#ffcc00")
    sg.fill_circle(cx, cy, size * 2)
    sg.set_fill_color("black")
    sg.fill_circle(cx, cy, size)

def draw_snowflake(cx, cy, size):
    sg.set_fill_color("white")
    sg.set_outline_color("#020210")
    sg.set_line_thickness(0)
    sg.fill_circle(cx, cy, size)

# Draws the trunk of the tree - Trinh
def draw_tree_trunk(x, y, width, height):
    sg.set_fill_color("#5c3d1e")
    sg.set_outline_color("#5c3d1e")
    sg.set_line_thickness(1)
    sg.fill_rectangle(x - width // 2, y, width, height)

# Draws the leafy top of the tree as stacked triangles - Trinh
def draw_tree_top(x, y, size):
    sg.set_fill_color("#1a4d2e")
    sg.set_outline_color("#1a4d2e")
    sg.set_line_thickness(1)
    sg.fill_triangle(x, y - size,       x - size, y + size // 2, x + size, y + size // 2)
    sg.fill_triangle(x, y - size * 1.5, x - size * 0.8, y,       x + size * 0.8, y)

# Draws the dark rocky body of a mountain - Bibu
def draw_mountain(cx, base_y, width, height):
    sg.set_fill_color("#2b2b3b")
    sg.set_outline_color("#2b2b3b")
    sg.set_line_thickness(1)
    sg.fill_triangle(cx, base_y - height, cx - width // 2, base_y, cx + width // 2, base_y)

# Draws a snow cap on the peak of a mountain - Bibu
def draw_mountain_snow_cap(cx, base_y, height, cap_size):
    cap_y = base_y - height
    sg.set_fill_color("#ddeeff")
    sg.set_outline_color("#ddeeff")
    sg.set_line_thickness(1)
    sg.fill_triangle(cx, cap_y, cx - cap_size, cap_y + cap_size * 2, cx + cap_size, cap_y + cap_size * 2)

def draw_picture(width, height):
    sg.fill_background("#020210")
    
    tiny_colors = ["#333366", "#4d4d80", "#5c5c8a"]
    for _ in range(600):
        rx = random.randint(0, width)
        ry = random.randint(0, height)
        rs = random.uniform(0.1, 0.8)
        rc = random.choice(tiny_colors)
        draw_point_star(rx, ry, rs, rc)
        
    star_colors = ["#ffffff", "#e6f2ff", "#fff7e6", "#ffe6cc"]
    for x in range(0, width, 2):
        center_y = (height - 50) - (x * 0.5)
        for _ in range(3):
            star_x = x + random.randint(-60, 60)
            star_y = center_y + random.randint(-50, 50)
            star_size = random.uniform(0.3, 1.5)
            star_color = random.choice(star_colors)
            draw_point_star(star_x, star_y, star_size, star_color)

    # Mountains in the background - Bibu
    draw_mountain(200,  height - 80, 400, 300)
    draw_mountain(550,  height - 80, 500, 380)
    draw_mountain(950,  height - 80, 420, 280)
    draw_mountain(1150, height - 80, 350, 320)

    # Snow caps on each mountain - Bibu
    draw_mountain_snow_cap(200,  height - 80, 300, 50)
    draw_mountain_snow_cap(550,  height - 80, 380, 65)
    draw_mountain_snow_cap(950,  height - 80, 280, 45)
    draw_mountain_snow_cap(1150, height - 80, 320, 55)

    # Moon - Bibu
    sg.draw_moon(random.randint(200,400), 100, 75)

    # Snow on the ground - Kesha
    sg.set_fill_color("#ddeeff")
    sg.set_outline_color("#ddeeff")
    sg.set_line_thickness(1)
    sg.fill_rectangle(0, height - 80, width, 80)

    # Soft snow drifts - Kesha
    for i in range(0, width, 4):
        drift_h = random.randint(10, 40)
        sg.set_fill_color("#eef4ff")
        sg.set_outline_color("#eef4ff")
        sg.fill_circle(i, height - 80, drift_h)

    # Two trees sitting on the snow - Trinh
    draw_tree_trunk(250, height - 140, 20, 60)
    draw_tree_top(250, height - 140, 60)

    draw_tree_trunk(900, height - 160, 24, 70)
    draw_tree_top(900, height - 160, 75)

    # Falling snowflakes - Kesha
    for _ in range(200):
        sx = random.randint(0, width)
        sy = random.randint(0, height - 80)
        ss = random.uniform(1, 4)
        draw_snowflake(sx, sy, ss)

if __name__ == "__main__":
    sg.start(draw_picture, 1200, 800)
