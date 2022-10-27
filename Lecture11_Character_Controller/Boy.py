from pico2d import *

# 이벤트 정의
RD, LD, RU, LU = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
}

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        self.events = None

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter()

    def update(self):
        self.cur_state.do()
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.Add_Q(key_event)
        if self.q:  # 리스트에 무언가 들어있으면
            event = self.q.pop()
            self.cur_state.exit()
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter()

    def Add_Q(self, key_event):
        self.q.insert(0, key_event)
        pass

        # for event in self.events:
        #     if event.type == SDL_KEYDOWN:
        #         match event.key:
        #             case pico2d.SDLK_LEFT:
        #                 self.dir -= 1
        #             case pico2d.SDLK_RIGHT:
        #                 self.dir += 1
        #     elif event.type == SDL_KEYUP:
        #         match event.key:
        #             case pico2d.SDLK_LEFT:
        #                 self.dir += 1
        #                 self.face_dir = -1
        #             case pico2d.SDLK_RIGHT:
        #                 self.dir -= 1
        #                 self.face_dir = 1
    pass

# 스테이트 구현

class IDLE:

    @staticmethod
    def enter():
        print('enter idle')
        pass

    @staticmethod
    def exit():
        print('exit idle')
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass

    pass

class RUN:
    @staticmethod
    def enter():
        print('enter run')

        pass

    @staticmethod
    def exit():
        print('exit run')
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass
    pass

next_state = {
    IDLE : {RU : RUN, LU : RUN, RD : RUN, LD : RUN},
    RUN : {RU : IDLE, LU: IDLE, IDLE : RUN, LD : IDLE}
}