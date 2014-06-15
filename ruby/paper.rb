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

    def parents
        curr = self
        l = []
        while curr
            l.push(curr)
            curr = curr.parent
        end
        l.reverse
    end

    def progression_map
        steps = self.parents.map { |x| x.pos }
        min = steps.first
        max = steps.last
        puts min,max
        Range.new(min.y, max.y).each do |y|
            Range.new(min.x, max.x).each do |x|
                curr = Vec.new(x, y)
                if steps.include? curr then
                    print 'x'
                else
                    print '.'
                end
            end
            puts
        end
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
        puts 'L:' + to_explore_next.size.to_s
        to_explore = to_explore_next
        to_explore_next = []
    end
end

sol = solve(Vec.new(0,0), Vec.new(12,8))
puts 'sol:'
puts sol.parents
puts 'map:'
sol.progression_map
