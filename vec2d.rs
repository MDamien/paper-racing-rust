use std::fmt;

pub struct Vec2 {
    pub x: int,
    pub y: int
}

impl Vec2 {
    pub fn new(x: int, y: int) -> Vec2{
        Vec2{x: x,y: y}
    }
}

impl Add<Vec2, Vec2> for Vec2 {
    fn add(&self, other: &Vec2) -> Vec2 {
        Vec2::new(self.x + other.x, self.y + other.y)
    }
}

impl PartialEq for Vec2 {
    fn eq(&self, other: &Vec2) -> bool{
        self.x == other.x && self.y == other.y
    }
}

impl fmt::Show for Vec2 {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({},{})", self.x, self.y)
    }
}

#[test]
fn test_add(){
    assert_eq!(Vec2::new(1,2) + Vec2::new(2,1), Vec2::new(3,3));
    assert_eq!(Vec2::new(1,2) + Vec2::new(-3,-1), Vec2::new(-2,1));
}
