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
    
    

    
def draw_picture(width, height):
    sg.fill_background("#020210")
    
    """ Nathan I used Generative ai for this part i recommend not changing it
    """
    
    tiny_colors = ["#333366", "#4d4d80", "#5c5c8a"]
    for _ in range(600):
        rx = random.randint(0, width)
        ry = random.randint(0, height)
        rs = random.uniform(0.1, 0.8)
        rc = random.choice(tiny_colors)
        draw_point_star (rx, ry, rs, rc)
        
    star_colors = ["#ffffff", "#e6f2ff", "#fff7e6", "#ffe6cc"]
    for x in range(0, width, 2):
        center_y = (height - 50) - (x * 0.5)
        for _ in range(3):
            star_x = x + random.randint(-60, 60)
            star_y = center_y + random.randint(-50, 50)
            star_size = random.uniform(0.3, 1.5)
            star_color = random.choice(star_colors)
            draw_point_star(star_x, star_y, star_size, star_color)
            

            
        
if __name__ == "__main__":
    sg.start(draw_picture, 1200, 800)


        
        
    


