from pico2d import *

def handle_events():
    global running
    global x, y
    events = get_events()
    # fill here



open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')



running = True
x, y = 100, 100
frame = 0
hide_cursor()
while (running):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    handle_events()

close_canvas()




