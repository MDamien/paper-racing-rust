extern crate debug;

use vec2d::Vec2;

mod vec2d;

struct State {
    pos: Vec2,
    vel: Vec2
}

impl State {
    fn choices(&self) -> Vec<State> {
        let mut choices = Vec::new();
        for dx in range(-1,2) {
            for dy in range(-1,2) {
                let state = State{
                    pos: self.pos + self.vel + Vec2::new(dx,dy),
                    vel: self.vel + Vec2::new(dx,dy)
                };
                choices.push(state);
            }
        }
        return choices;
    }
}

fn main() {
    let mut to_explore = Vec::new(); 
    let mut to_explore_next = Vec::new(); 

    let start = State{
        pos: Vec2::new(0,0),
        vel: Vec2::new(0,0)
    };
    to_explore.push(start);

    let goal = Vec2::new(20,7);
    
    loop {
        println!("L:{}", to_explore.len());
        for state in to_explore.iter() {
            if state.pos == goal{
                println!("Yeahh!");
                return;
            }
            for choice in state.choices().iter() {
                to_explore_next.push(*choice);
            }
        }
        to_explore = to_explore_next;
        to_explore_next = Vec::new();
    }
}

