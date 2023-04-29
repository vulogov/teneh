extern crate pest;
use crate::lang::Rule;

use crate::vm::unknown;
use crate::vm::eoi;




pub fn parse_pair(p: pest::iterators::Pair<Rule>) {
    let rule  = &p.as_rule();
    let token = &p.as_span();
    match rule {
        Rule::EOI => {
            eoi::process_token(&p, &token.as_str().to_string());
        }
        _ => {
            unknown::process_token(&p, &token.as_str().to_string());
        }
    }
}
