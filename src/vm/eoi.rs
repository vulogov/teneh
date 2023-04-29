extern crate log;
extern crate pest;
use crate::lang::Rule;

pub fn process_token(p: &pest::iterators::Pair<Rule>, _t: &String) {
    log::debug!("Received EOI token: {:#?}", p.as_rule());
}
