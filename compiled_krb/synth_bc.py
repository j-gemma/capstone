# synth_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def complete_module2(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'input_type', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.complete_module2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_type', context,
                              (rule.pattern(0),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(6),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.complete_module2: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'pd_object', context,
                                  (rule.pattern(0),
                                   rule.pattern(7),
                                   rule.pattern(8),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "synth.complete_module2: got unexpected plan from when clause 3"
                    with engine.prove('synthesizer', 'gene_value', context,
                                      (rule.pattern(0),
                                       rule.pattern(9),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "synth.complete_module2: got unexpected plan from when clause 4"
                        with engine.prove(rule.rule_base.root_name, 'output_type', context,
                                          (rule.pattern(0),
                                           rule.pattern(10),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "synth.complete_module2: got unexpected plan from when clause 5"
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def param_in(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'connected', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.param_in: got unexpected plan from when clause 1"
            with engine.prove('synthesizer', 'output_type', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.param_in: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def in_type(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'connected', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.in_type: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'output_type', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.in_type: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def three_inputs(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'input_type', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.three_inputs: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_type', context,
                              (rule.pattern(0),
                               rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.three_inputs: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'input_type', context,
                                  (rule.pattern(0),
                                   rule.pattern(5),
                                   rule.pattern(6),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "synth.three_inputs: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def two_inputs(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'input_type', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.two_inputs: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_type', context,
                              (rule.pattern(0),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(6),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.two_inputs: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def heck(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'input_type', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.heck: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_type', context,
                              (rule.pattern(0),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(6),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.heck: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def param_s(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'output_type', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.param_s: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def param_c(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'output_type', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.param_c: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def control_out(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'pd_object', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.control_out: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def signal_out(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'pd_object', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.signal_out: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc0(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc0: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc0: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc0(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc0: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc0: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs0(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs0: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs0: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss0(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss0: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss0: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc1(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc1: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc1(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc1: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs1(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs1: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss1(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss1: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc2(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc2: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc2(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc2: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs2(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs2: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss2(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss2: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc3(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc3: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc3(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc3: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs3(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs3: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss3(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss3: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc4(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc4: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc4: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc4(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc4: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc4: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs4(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs4: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs4: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss4(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss4: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss4: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cos(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cos: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def phasor(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.phasor: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.phasor: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def noise(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.noise: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc8(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc8: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc8: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc8(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc8: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc8: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs8(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs8: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs8: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss8(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss8: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss8: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc9(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc9: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc9: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc9(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc9: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc9: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs9(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs9: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs9: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss9(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss9: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss9: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc10(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc10: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc10: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc10(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc10: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc10: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs10(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs10: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs10: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss10(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss10: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss10: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc11(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc11: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc11: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc11(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc11: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc11: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs11(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs11: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs11: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss11(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss11: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss11: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc12(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc12: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc12: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc12(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc12: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc12: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs12(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs12: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs12: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss12(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss12: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss12: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc13(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc13: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc13: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc13(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc13: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc13: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs13(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs13: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs13: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss13(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss13: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss13: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cc14(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cc14: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cc14: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def sc14(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.sc14: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.sc14: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cs14(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.cs14: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.cs14: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ss14(rule, arg_patterns, arg_context):
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
        with engine.prove('synthesizer', 'gene_value', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.ss14: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'input_types', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.ss14: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('synth')
  
  bc_rule.bc_rule('complete_module2', This_rule_base, 'complete_module2',
                  complete_module2, None,
                  (contexts.variable('index'),
                   contexts.variable('type1'),
                   contexts.variable('connected_module1'),
                   contexts.variable('type2'),
                   contexts.variable('connected_module2'),
                   contexts.variable('pd_object'),
                   contexts.variable('gene_value'),
                   contexts.variable('output_type'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(1),
                   contexts.variable('type1'),
                   contexts.variable('connected_module1'),
                   pattern.pattern_literal(2),
                   contexts.variable('type2'),
                   contexts.variable('connected_module2'),
                   contexts.variable('pd_object'),
                   contexts.variable('output_type'),
                   contexts.variable('gene_value'),
                   contexts.variable('type'),))
  
  bc_rule.bc_rule('param_in', This_rule_base, 'input_type',
                  param_in, None,
                  (contexts.variable('current_module'),
                   contexts.variable('input_index'),
                   contexts.variable('type'),
                   contexts.variable('connected_module'),),
                  (),
                  (contexts.variable('current_module'),
                   contexts.variable('input_index'),
                   contexts.variable('connected_module'),
                   contexts.variable('type'),))
  
  bc_rule.bc_rule('in_type', This_rule_base, 'input_type',
                  in_type, None,
                  (contexts.variable('current_module'),
                   contexts.variable('input_index'),
                   contexts.variable('type'),
                   contexts.variable('connected_module'),),
                  (),
                  (contexts.variable('current_module'),
                   contexts.variable('input_index'),
                   contexts.variable('connected_module'),
                   contexts.variable('type'),))
  
  bc_rule.bc_rule('three_inputs', This_rule_base, 'three_inputs',
                  three_inputs, None,
                  (contexts.variable('index'),
                   contexts.variable('type1'),
                   contexts.variable('type2'),
                   contexts.variable('type3'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(1),
                   contexts.variable('type1'),
                   pattern.pattern_literal(2),
                   contexts.variable('type2'),
                   pattern.pattern_literal(3),
                   contexts.variable('type3'),))
  
  bc_rule.bc_rule('two_inputs', This_rule_base, 'input_types',
                  two_inputs, None,
                  (contexts.variable('current_module'),
                   contexts.variable('type1'),
                   contexts.variable('type2'),),
                  (),
                  (contexts.variable('current_module'),
                   pattern.pattern_literal(1),
                   contexts.variable('type1'),
                   contexts.variable('connection1'),
                   pattern.pattern_literal(2),
                   contexts.variable('type2'),
                   contexts.variable('connection2'),))
  
  bc_rule.bc_rule('heck', This_rule_base, 'input_types_connections',
                  heck, None,
                  (contexts.variable('current_module'),
                   contexts.variable('type1'),
                   contexts.variable('connection1'),
                   contexts.variable('type2'),
                   contexts.variable('connection2'),),
                  (),
                  (contexts.variable('current_module'),
                   pattern.pattern_literal(1),
                   contexts.variable('type1'),
                   contexts.variable('connection1'),
                   pattern.pattern_literal(2),
                   contexts.variable('type2'),
                   contexts.variable('connection2'),))
  
  bc_rule.bc_rule('param_s', This_rule_base, 'output_type',
                  param_s, None,
                  (contexts.variable('current_module'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('current_module'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('param_c', This_rule_base, 'output_type',
                  param_c, None,
                  (contexts.variable('current_module'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('current_module'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('control_out', This_rule_base, 'output_type',
                  control_out, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   contexts.variable('id'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('signal_out', This_rule_base, 'output_type',
                  signal_out, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   contexts.variable('id'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc0', This_rule_base, 'pd_object',
                  cc0, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc0', This_rule_base, 'pd_object',
                  sc0, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs0', This_rule_base, 'pd_object',
                  cs0, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss0', This_rule_base, 'pd_object',
                  ss0, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc1', This_rule_base, 'pd_object',
                  cc1, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc1', This_rule_base, 'pd_object',
                  sc1, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs1', This_rule_base, 'pd_object',
                  cs1, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss1', This_rule_base, 'pd_object',
                  ss1, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc2', This_rule_base, 'pd_object',
                  cc2, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc2', This_rule_base, 'pd_object',
                  sc2, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs2', This_rule_base, 'pd_object',
                  cs2, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss2', This_rule_base, 'pd_object',
                  ss2, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(0),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc3', This_rule_base, 'pd_object',
                  cc3, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(3),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc3', This_rule_base, 'pd_object',
                  sc3, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(3),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs3', This_rule_base, 'pd_object',
                  cs3, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(3),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss3', This_rule_base, 'pd_object',
                  ss3, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(3),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc4', This_rule_base, 'pd_object',
                  cc4, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('osc'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(4),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc4', This_rule_base, 'pd_object',
                  sc4, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('osc~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(4),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs4', This_rule_base, 'pd_object',
                  cs4, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('osc~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(4),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss4', This_rule_base, 'pd_object',
                  ss4, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('osc~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(4),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cos', This_rule_base, 'pd_object',
                  cos, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('cos~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(5),))
  
  bc_rule.bc_rule('phasor', This_rule_base, 'pd_object',
                  phasor, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('phasor~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(6),
                   pattern.pattern_literal('c'),
                   contexts.variable('type2'),))
  
  bc_rule.bc_rule('noise', This_rule_base, 'pd_object',
                  noise, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('noise~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(7),))
  
  bc_rule.bc_rule('cc8', This_rule_base, 'pd_object',
                  cc8, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('lop'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(8),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc8', This_rule_base, 'pd_object',
                  sc8, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('lop~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(8),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs8', This_rule_base, 'pd_object',
                  cs8, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('lop~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(8),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss8', This_rule_base, 'pd_object',
                  ss8, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('lop~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(8),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc9', This_rule_base, 'pd_object',
                  cc9, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('hip'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(9),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc9', This_rule_base, 'pd_object',
                  sc9, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('hip~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(9),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs9', This_rule_base, 'pd_object',
                  cs9, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('hip~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(9),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss9', This_rule_base, 'pd_object',
                  ss9, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('hip~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(9),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc10', This_rule_base, 'pd_object',
                  cc10, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('vcf'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(10),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc10', This_rule_base, 'pd_object',
                  sc10, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('vcf~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(10),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs10', This_rule_base, 'pd_object',
                  cs10, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('vcf~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(10),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss10', This_rule_base, 'pd_object',
                  ss10, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('vcf~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(10),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc11', This_rule_base, 'pd_object',
                  cc11, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(11),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc11', This_rule_base, 'pd_object',
                  sc11, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(11),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs11', This_rule_base, 'pd_object',
                  cs11, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(11),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss11', This_rule_base, 'pd_object',
                  ss11, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('+~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(11),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc12', This_rule_base, 'pd_object',
                  cc12, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(12),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc12', This_rule_base, 'pd_object',
                  sc12, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(12),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs12', This_rule_base, 'pd_object',
                  cs12, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(12),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss12', This_rule_base, 'pd_object',
                  ss12, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(12),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc13', This_rule_base, 'pd_object',
                  cc13, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(13),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc13', This_rule_base, 'pd_object',
                  sc13, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(13),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs13', This_rule_base, 'pd_object',
                  cs13, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(13),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss13', This_rule_base, 'pd_object',
                  ss13, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(13),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc14', This_rule_base, 'pd_object',
                  cc14, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(14),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc14', This_rule_base, 'pd_object',
                  sc14, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(14),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs14', This_rule_base, 'pd_object',
                  cs14, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(14),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss14', This_rule_base, 'pd_object',
                  ss14, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('/~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(14),
                   pattern.pattern_literal('s'),))


Krb_filename = '..\\synth.krb'
Krb_lineno_map = (
    ((14, 18), (5, 5)),
    ((20, 28), (7, 7)),
    ((29, 37), (8, 8)),
    ((38, 45), (9, 9)),
    ((46, 52), (10, 10)),
    ((53, 59), (11, 11)),
    ((72, 76), (14, 14)),
    ((78, 85), (16, 16)),
    ((86, 92), (17, 17)),
    ((105, 109), (20, 20)),
    ((111, 118), (22, 22)),
    ((119, 125), (23, 23)),
    ((138, 142), (26, 26)),
    ((144, 151), (28, 28)),
    ((152, 159), (29, 29)),
    ((160, 167), (30, 30)),
    ((180, 184), (33, 33)),
    ((186, 194), (35, 35)),
    ((195, 203), (36, 36)),
    ((216, 220), (39, 39)),
    ((222, 230), (41, 41)),
    ((231, 239), (42, 42)),
    ((252, 256), (45, 45)),
    ((258, 264), (47, 47)),
    ((277, 281), (50, 50)),
    ((283, 289), (52, 52)),
    ((302, 306), (55, 55)),
    ((308, 315), (57, 57)),
    ((328, 332), (60, 60)),
    ((334, 341), (62, 62)),
    ((354, 358), (65, 65)),
    ((360, 366), (67, 67)),
    ((367, 374), (68, 68)),
    ((387, 391), (71, 71)),
    ((393, 399), (73, 73)),
    ((400, 407), (74, 74)),
    ((420, 424), (77, 77)),
    ((426, 432), (79, 79)),
    ((433, 440), (80, 80)),
    ((453, 457), (83, 83)),
    ((459, 465), (85, 85)),
    ((466, 473), (86, 86)),
    ((486, 490), (89, 89)),
    ((492, 498), (91, 91)),
    ((499, 506), (92, 92)),
    ((519, 523), (95, 95)),
    ((525, 531), (97, 97)),
    ((532, 539), (98, 98)),
    ((552, 556), (101, 101)),
    ((558, 564), (103, 103)),
    ((565, 572), (104, 104)),
    ((585, 589), (107, 107)),
    ((591, 597), (109, 109)),
    ((598, 605), (110, 110)),
    ((618, 622), (113, 113)),
    ((624, 630), (115, 115)),
    ((631, 638), (116, 116)),
    ((651, 655), (119, 119)),
    ((657, 663), (121, 121)),
    ((664, 671), (122, 122)),
    ((684, 688), (125, 125)),
    ((690, 696), (127, 127)),
    ((697, 704), (128, 128)),
    ((717, 721), (131, 131)),
    ((723, 729), (133, 133)),
    ((730, 737), (134, 134)),
    ((750, 754), (137, 137)),
    ((756, 762), (139, 139)),
    ((763, 770), (140, 140)),
    ((783, 787), (143, 143)),
    ((789, 795), (145, 145)),
    ((796, 803), (146, 146)),
    ((816, 820), (149, 149)),
    ((822, 828), (151, 151)),
    ((829, 836), (152, 152)),
    ((849, 853), (155, 155)),
    ((855, 861), (157, 157)),
    ((862, 869), (158, 158)),
    ((882, 886), (161, 161)),
    ((888, 894), (163, 163)),
    ((895, 902), (164, 164)),
    ((915, 919), (167, 167)),
    ((921, 927), (169, 169)),
    ((928, 935), (170, 170)),
    ((948, 952), (173, 173)),
    ((954, 960), (175, 175)),
    ((961, 968), (176, 176)),
    ((981, 985), (179, 179)),
    ((987, 993), (181, 181)),
    ((994, 1001), (182, 182)),
    ((1014, 1018), (185, 185)),
    ((1020, 1026), (187, 187)),
    ((1039, 1043), (190, 190)),
    ((1045, 1051), (192, 192)),
    ((1052, 1059), (193, 193)),
    ((1072, 1076), (196, 196)),
    ((1078, 1084), (198, 198)),
    ((1097, 1101), (201, 201)),
    ((1103, 1109), (203, 203)),
    ((1110, 1117), (204, 204)),
    ((1130, 1134), (207, 207)),
    ((1136, 1142), (209, 209)),
    ((1143, 1150), (210, 210)),
    ((1163, 1167), (213, 213)),
    ((1169, 1175), (215, 215)),
    ((1176, 1183), (216, 216)),
    ((1196, 1200), (219, 219)),
    ((1202, 1208), (221, 221)),
    ((1209, 1216), (222, 222)),
    ((1229, 1233), (225, 225)),
    ((1235, 1241), (227, 227)),
    ((1242, 1249), (228, 228)),
    ((1262, 1266), (231, 231)),
    ((1268, 1274), (233, 233)),
    ((1275, 1282), (234, 234)),
    ((1295, 1299), (237, 237)),
    ((1301, 1307), (239, 239)),
    ((1308, 1315), (240, 240)),
    ((1328, 1332), (243, 243)),
    ((1334, 1340), (245, 245)),
    ((1341, 1348), (246, 246)),
    ((1361, 1365), (249, 249)),
    ((1367, 1373), (251, 251)),
    ((1374, 1381), (252, 252)),
    ((1394, 1398), (255, 255)),
    ((1400, 1406), (257, 257)),
    ((1407, 1414), (258, 258)),
    ((1427, 1431), (261, 261)),
    ((1433, 1439), (263, 263)),
    ((1440, 1447), (264, 264)),
    ((1460, 1464), (267, 267)),
    ((1466, 1472), (269, 269)),
    ((1473, 1480), (270, 270)),
    ((1493, 1497), (273, 273)),
    ((1499, 1505), (275, 275)),
    ((1506, 1513), (276, 276)),
    ((1526, 1530), (279, 279)),
    ((1532, 1538), (281, 281)),
    ((1539, 1546), (282, 282)),
    ((1559, 1563), (285, 285)),
    ((1565, 1571), (287, 287)),
    ((1572, 1579), (288, 288)),
    ((1592, 1596), (291, 291)),
    ((1598, 1604), (293, 293)),
    ((1605, 1612), (294, 294)),
    ((1625, 1629), (297, 297)),
    ((1631, 1637), (299, 299)),
    ((1638, 1645), (300, 300)),
    ((1658, 1662), (303, 303)),
    ((1664, 1670), (305, 305)),
    ((1671, 1678), (306, 306)),
    ((1691, 1695), (309, 309)),
    ((1697, 1703), (311, 311)),
    ((1704, 1711), (312, 312)),
    ((1724, 1728), (315, 315)),
    ((1730, 1736), (317, 317)),
    ((1737, 1744), (318, 318)),
    ((1757, 1761), (321, 321)),
    ((1763, 1769), (323, 323)),
    ((1770, 1777), (324, 324)),
    ((1790, 1794), (327, 327)),
    ((1796, 1802), (329, 329)),
    ((1803, 1810), (330, 330)),
    ((1823, 1827), (333, 333)),
    ((1829, 1835), (335, 335)),
    ((1836, 1843), (336, 336)),
    ((1856, 1860), (339, 339)),
    ((1862, 1868), (341, 341)),
    ((1869, 1876), (342, 342)),
    ((1889, 1893), (345, 345)),
    ((1895, 1901), (347, 347)),
    ((1902, 1909), (348, 348)),
    ((1922, 1926), (351, 351)),
    ((1928, 1934), (353, 353)),
    ((1935, 1942), (354, 354)),
    ((1955, 1959), (357, 357)),
    ((1961, 1967), (359, 359)),
    ((1968, 1975), (360, 360)),
    ((1988, 1992), (363, 363)),
    ((1994, 2000), (365, 365)),
    ((2001, 2008), (366, 366)),
)
