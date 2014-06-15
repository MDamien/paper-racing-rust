require 'vector2d'
Vec = Vector2d

class State
    attr_reader :pos, :vel, :parent
    
    def initialize(pos, vel, parent=nil)
        @pos, @vel, @parent = pos, vel, parent
    end

    def choices
        l = []
        (-1..1).each do |dx|
            (-1..1).each do |dy|
                l.push(State.new(@pos + @vel + Vec.new(dx, dy),
                    @vel + Vec.new(dx, dy), self))
            end
        end
        l
    end

    def to_s
        @pos.to_s + '-' + @vel.to_s  
    end

    def steps
        if parent then parent.steps end
        puts @pos
    end
end


def solve(start, goal)
    state = State.new start, Vec.new(0,0)
    to_explore = [state]
    to_explore_next = []
    while true
        for state in to_explore
            if state.pos == goal then
                return state
            end
            to_explore_next += state.choices
        end
        to_explore = to_explore_next
        to_explore_next = []
    end
end

solve(Vec.new(0,0), Vec.new(10,10)).steps
