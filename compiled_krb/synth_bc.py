# synth_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def test_complete_module2(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'input_types_connections', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.test_complete_module2: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def test_pd_obj(rule, arg_patterns, arg_context):
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
              "synth.test_pd_obj: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

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
        with engine.prove(rule.rule_base.root_name, 'input_types_connections', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "synth.complete_module2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'pd_object', context,
                              (rule.pattern(0),
                               rule.pattern(5),
                               rule.pattern(6),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "synth.complete_module2: got unexpected plan from when clause 2"
                with engine.prove('synthesizer', 'gene_value', context,
                                  (rule.pattern(0),
                                   rule.pattern(7),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "synth.complete_module2: got unexpected plan from when clause 3"
                    with engine.prove(rule.rule_base.root_name, 'output_type', context,
                                      (rule.pattern(0),
                                       rule.pattern(8),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "synth.complete_module2: got unexpected plan from when clause 4"
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
  
  bc_rule.bc_rule('test_complete_module2', This_rule_base, 'acomplete_module2',
                  test_complete_module2, None,
                  (contexts.variable('index'),
                   contexts.variable('type1'),
                   contexts.variable('connected_module1'),
                   contexts.variable('type2'),
                   contexts.variable('connected_module2'),),
                  (),
                  (contexts.variable('index'),
                   contexts.variable('type1'),
                   contexts.variable('connected_module1'),
                   contexts.variable('type2'),
                   contexts.variable('connected_module2'),))
  
  bc_rule.bc_rule('test_pd_obj', This_rule_base, 'bcomplete_module2',
                  test_pd_obj, None,
                  (contexts.variable('index'),
                   contexts.variable('pd_object'),
                   contexts.variable('output_type'),),
                  (),
                  (contexts.variable('index'),
                   contexts.variable('pd_object'),
                   pattern.pattern_literal('output_type'),))
  
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
                   contexts.variable('type1'),
                   contexts.variable('connected_module1'),
                   contexts.variable('type2'),
                   contexts.variable('connected_module2'),
                   contexts.variable('pd_object'),
                   contexts.variable('output_type'),
                   contexts.variable('gene_value'),
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
                   pattern.pattern_literal(1),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc1', This_rule_base, 'pd_object',
                  sc1, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(1),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs1', This_rule_base, 'pd_object',
                  cs1, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(1),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss1', This_rule_base, 'pd_object',
                  ss1, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('-~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(1),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('cc2', This_rule_base, 'pd_object',
                  cc2, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(2),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('sc2', This_rule_base, 'pd_object',
                  sc2, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(2),
                   pattern.pattern_literal('s'),
                   pattern.pattern_literal('c'),))
  
  bc_rule.bc_rule('cs2', This_rule_base, 'pd_object',
                  cs2, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('s'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(2),
                   pattern.pattern_literal('c'),
                   pattern.pattern_literal('s'),))
  
  bc_rule.bc_rule('ss2', This_rule_base, 'pd_object',
                  ss2, None,
                  (contexts.variable('index'),
                   pattern.pattern_literal('*~'),
                   pattern.pattern_literal('c'),),
                  (),
                  (contexts.variable('index'),
                   pattern.pattern_literal(2),
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
    ((14, 18), (3, 3)),
    ((20, 29), (5, 5)),
    ((42, 46), (8, 8)),
    ((48, 55), (10, 10)),
    ((68, 72), (13, 13)),
    ((74, 83), (15, 15)),
    ((84, 91), (16, 16)),
    ((92, 98), (17, 17)),
    ((99, 105), (18, 18)),
    ((118, 122), (27, 27)),
    ((124, 131), (29, 29)),
    ((132, 138), (30, 30)),
    ((151, 155), (33, 33)),
    ((157, 164), (35, 35)),
    ((165, 172), (36, 36)),
    ((173, 180), (37, 37)),
    ((193, 197), (40, 40)),
    ((199, 207), (42, 42)),
    ((208, 216), (43, 43)),
    ((229, 233), (46, 46)),
    ((235, 243), (48, 48)),
    ((244, 252), (49, 49)),
    ((265, 269), (52, 52)),
    ((271, 277), (54, 54)),
    ((290, 294), (57, 57)),
    ((296, 302), (59, 59)),
    ((315, 319), (62, 62)),
    ((321, 328), (64, 64)),
    ((341, 345), (67, 67)),
    ((347, 354), (69, 69)),
    ((367, 371), (72, 72)),
    ((373, 379), (74, 74)),
    ((380, 387), (75, 75)),
    ((400, 404), (78, 78)),
    ((406, 412), (80, 80)),
    ((413, 420), (81, 81)),
    ((433, 437), (84, 84)),
    ((439, 445), (86, 86)),
    ((446, 453), (87, 87)),
    ((466, 470), (90, 90)),
    ((472, 478), (92, 92)),
    ((479, 486), (93, 93)),
    ((499, 503), (96, 96)),
    ((505, 511), (98, 98)),
    ((512, 519), (99, 99)),
    ((532, 536), (102, 102)),
    ((538, 544), (104, 104)),
    ((545, 552), (105, 105)),
    ((565, 569), (108, 108)),
    ((571, 577), (110, 110)),
    ((578, 585), (111, 111)),
    ((598, 602), (114, 114)),
    ((604, 610), (116, 116)),
    ((611, 618), (117, 117)),
    ((631, 635), (120, 120)),
    ((637, 643), (122, 122)),
    ((644, 651), (123, 123)),
    ((664, 668), (126, 126)),
    ((670, 676), (128, 128)),
    ((677, 684), (129, 129)),
    ((697, 701), (132, 132)),
    ((703, 709), (134, 134)),
    ((710, 717), (135, 135)),
    ((730, 734), (138, 138)),
    ((736, 742), (140, 140)),
    ((743, 750), (141, 141)),
    ((763, 767), (144, 144)),
    ((769, 775), (146, 146)),
    ((776, 783), (147, 147)),
    ((796, 800), (150, 150)),
    ((802, 808), (152, 152)),
    ((809, 816), (153, 153)),
    ((829, 833), (156, 156)),
    ((835, 841), (158, 158)),
    ((842, 849), (159, 159)),
    ((862, 866), (162, 162)),
    ((868, 874), (164, 164)),
    ((875, 882), (165, 165)),
    ((895, 899), (168, 168)),
    ((901, 907), (170, 170)),
    ((908, 915), (171, 171)),
    ((928, 932), (174, 174)),
    ((934, 940), (176, 176)),
    ((941, 948), (177, 177)),
    ((961, 965), (180, 180)),
    ((967, 973), (182, 182)),
    ((974, 981), (183, 183)),
    ((994, 998), (186, 186)),
    ((1000, 1006), (188, 188)),
    ((1007, 1014), (189, 189)),
    ((1027, 1031), (192, 192)),
    ((1033, 1039), (194, 194)),
    ((1052, 1056), (197, 197)),
    ((1058, 1064), (199, 199)),
    ((1065, 1072), (200, 200)),
    ((1085, 1089), (203, 203)),
    ((1091, 1097), (205, 205)),
    ((1110, 1114), (208, 208)),
    ((1116, 1122), (210, 210)),
    ((1123, 1130), (211, 211)),
    ((1143, 1147), (214, 214)),
    ((1149, 1155), (216, 216)),
    ((1156, 1163), (217, 217)),
    ((1176, 1180), (220, 220)),
    ((1182, 1188), (222, 222)),
    ((1189, 1196), (223, 223)),
    ((1209, 1213), (226, 226)),
    ((1215, 1221), (228, 228)),
    ((1222, 1229), (229, 229)),
    ((1242, 1246), (232, 232)),
    ((1248, 1254), (234, 234)),
    ((1255, 1262), (235, 235)),
    ((1275, 1279), (238, 238)),
    ((1281, 1287), (240, 240)),
    ((1288, 1295), (241, 241)),
    ((1308, 1312), (244, 244)),
    ((1314, 1320), (246, 246)),
    ((1321, 1328), (247, 247)),
    ((1341, 1345), (250, 250)),
    ((1347, 1353), (252, 252)),
    ((1354, 1361), (253, 253)),
    ((1374, 1378), (256, 256)),
    ((1380, 1386), (258, 258)),
    ((1387, 1394), (259, 259)),
    ((1407, 1411), (262, 262)),
    ((1413, 1419), (264, 264)),
    ((1420, 1427), (265, 265)),
    ((1440, 1444), (268, 268)),
    ((1446, 1452), (270, 270)),
    ((1453, 1460), (271, 271)),
    ((1473, 1477), (274, 274)),
    ((1479, 1485), (276, 276)),
    ((1486, 1493), (277, 277)),
    ((1506, 1510), (280, 280)),
    ((1512, 1518), (282, 282)),
    ((1519, 1526), (283, 283)),
    ((1539, 1543), (286, 286)),
    ((1545, 1551), (288, 288)),
    ((1552, 1559), (289, 289)),
    ((1572, 1576), (292, 292)),
    ((1578, 1584), (294, 294)),
    ((1585, 1592), (295, 295)),
    ((1605, 1609), (298, 298)),
    ((1611, 1617), (300, 300)),
    ((1618, 1625), (301, 301)),
    ((1638, 1642), (304, 304)),
    ((1644, 1650), (306, 306)),
    ((1651, 1658), (307, 307)),
    ((1671, 1675), (310, 310)),
    ((1677, 1683), (312, 312)),
    ((1684, 1691), (313, 313)),
    ((1704, 1708), (316, 316)),
    ((1710, 1716), (318, 318)),
    ((1717, 1724), (319, 319)),
    ((1737, 1741), (322, 322)),
    ((1743, 1749), (324, 324)),
    ((1750, 1757), (325, 325)),
    ((1770, 1774), (328, 328)),
    ((1776, 1782), (330, 330)),
    ((1783, 1790), (331, 331)),
    ((1803, 1807), (334, 334)),
    ((1809, 1815), (336, 336)),
    ((1816, 1823), (337, 337)),
    ((1836, 1840), (340, 340)),
    ((1842, 1848), (342, 342)),
    ((1849, 1856), (343, 343)),
    ((1869, 1873), (346, 346)),
    ((1875, 1881), (348, 348)),
    ((1882, 1889), (349, 349)),
    ((1902, 1906), (352, 352)),
    ((1908, 1914), (354, 354)),
    ((1915, 1922), (355, 355)),
    ((1935, 1939), (358, 358)),
    ((1941, 1947), (360, 360)),
    ((1948, 1955), (361, 361)),
    ((1968, 1972), (364, 364)),
    ((1974, 1980), (366, 366)),
    ((1981, 1988), (367, 367)),
    ((2001, 2005), (370, 370)),
    ((2007, 2013), (372, 372)),
    ((2014, 2021), (373, 373)),
)
