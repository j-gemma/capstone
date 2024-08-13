# synth_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def input_type(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('synth', 'connected', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.input_type: got unexpected plan from when clause 1"
            with engine.prove('synth', 'output_type', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.input_type: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('synth')
  
  bc_rule.bc_rule('input_type', This_rule_base, 'input_type',
                  input_type, None,
                  (pattern.pattern_literal('current_module'),
                   pattern.pattern_literal('input_index'),
                   contexts.variable('c_or_s'),),
                  (),
                  (pattern.pattern_literal('current_module'),
                   pattern.pattern_literal('input_index'),
                   pattern.pattern_literal('connected_module'),
                   contexts.variable('c_or_s'),))


Krb_filename = '..\\synth.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 27), (6, 6)),
    ((28, 34), (7, 7)),
)
