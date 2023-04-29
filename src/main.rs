use better_panic;
pub mod cmd;
pub mod stdlib;
pub mod lang;
pub mod vm;

fn main() {
    better_panic::install();
    cmd::init();
}
