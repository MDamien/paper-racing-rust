from geom import Vec2D as Vec

class State:
    attrs :pos, :vec, :parent

    def choices:
        for dx in -1..1:
            for dy in -1..1:
                yield State(
                    pos = @pos + @vel + Vec(dx, dy),
                    vel = @vel + Vec(dx, dy)
                )

    def __str__:
        "{}-{}".format @pos, @vec

    def parents:
        curr = self
        while curr:
            yield curr
            curr = curr.parent


def solve(start, goal):
    to_explore = [State(start, Vec())]
    to_explore_next = []
    while True:
        for state in to_explore:
            if state.pos == goal: return state
            to_explore_next += state.choices
        to_explore, to_explore_next = to_explore_next, []
        print 'L:', to_explore.len()


sol = solve Vec(1,2) Vec(10,10)
print sol.parents()
