# synth_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

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
    ((14, 18), (9, 9)),
    ((20, 27), (11, 11)),
    ((40, 44), (14, 14)),
    ((46, 55), (16, 16)),
    ((56, 63), (17, 17)),
    ((64, 70), (18, 18)),
    ((71, 77), (19, 19)),
    ((90, 94), (28, 28)),
    ((96, 103), (30, 30)),
    ((104, 110), (31, 31)),
    ((123, 127), (34, 34)),
    ((129, 136), (36, 36)),
    ((137, 144), (37, 37)),
    ((145, 152), (38, 38)),
    ((165, 169), (41, 41)),
    ((171, 179), (43, 43)),
    ((180, 188), (44, 44)),
    ((201, 205), (47, 47)),
    ((207, 215), (49, 49)),
    ((216, 224), (50, 50)),
    ((237, 241), (53, 53)),
    ((243, 249), (55, 55)),
    ((262, 266), (58, 58)),
    ((268, 274), (60, 60)),
    ((287, 291), (63, 63)),
    ((293, 300), (65, 65)),
    ((313, 317), (68, 68)),
    ((319, 326), (70, 70)),
    ((339, 343), (74, 74)),
    ((345, 351), (76, 76)),
    ((352, 359), (77, 77)),
    ((372, 376), (80, 80)),
    ((378, 384), (82, 82)),
    ((385, 392), (83, 83)),
    ((405, 409), (86, 86)),
    ((411, 417), (88, 88)),
    ((418, 425), (89, 89)),
    ((438, 442), (92, 92)),
    ((444, 450), (94, 94)),
    ((451, 458), (95, 95)),
    ((471, 475), (98, 98)),
    ((477, 483), (100, 100)),
    ((484, 491), (101, 101)),
    ((504, 508), (104, 104)),
    ((510, 516), (106, 106)),
    ((517, 524), (107, 107)),
    ((537, 541), (110, 110)),
    ((543, 549), (112, 112)),
    ((550, 557), (113, 113)),
    ((570, 574), (116, 116)),
    ((576, 582), (118, 118)),
    ((583, 590), (119, 119)),
    ((603, 607), (122, 122)),
    ((609, 615), (124, 124)),
    ((616, 623), (125, 125)),
    ((636, 640), (128, 128)),
    ((642, 648), (130, 130)),
    ((649, 656), (131, 131)),
    ((669, 673), (134, 134)),
    ((675, 681), (136, 136)),
    ((682, 689), (137, 137)),
    ((702, 706), (140, 140)),
    ((708, 714), (142, 142)),
    ((715, 722), (143, 143)),
    ((735, 739), (146, 146)),
    ((741, 747), (148, 148)),
    ((748, 755), (149, 149)),
    ((768, 772), (152, 152)),
    ((774, 780), (154, 154)),
    ((781, 788), (155, 155)),
    ((801, 805), (158, 158)),
    ((807, 813), (160, 160)),
    ((814, 821), (161, 161)),
    ((834, 838), (164, 164)),
    ((840, 846), (166, 166)),
    ((847, 854), (167, 167)),
    ((867, 871), (170, 170)),
    ((873, 879), (172, 172)),
    ((880, 887), (173, 173)),
    ((900, 904), (176, 176)),
    ((906, 912), (178, 178)),
    ((913, 920), (179, 179)),
    ((933, 937), (182, 182)),
    ((939, 945), (184, 184)),
    ((946, 953), (185, 185)),
    ((966, 970), (188, 188)),
    ((972, 978), (190, 190)),
    ((979, 986), (191, 191)),
    ((999, 1003), (194, 194)),
    ((1005, 1011), (196, 196)),
    ((1024, 1028), (199, 199)),
    ((1030, 1036), (201, 201)),
    ((1037, 1044), (202, 202)),
    ((1057, 1061), (205, 205)),
    ((1063, 1069), (207, 207)),
    ((1082, 1086), (210, 210)),
    ((1088, 1094), (212, 212)),
    ((1095, 1102), (213, 213)),
    ((1115, 1119), (216, 216)),
    ((1121, 1127), (218, 218)),
    ((1128, 1135), (219, 219)),
    ((1148, 1152), (222, 222)),
    ((1154, 1160), (224, 224)),
    ((1161, 1168), (225, 225)),
    ((1181, 1185), (228, 228)),
    ((1187, 1193), (230, 230)),
    ((1194, 1201), (231, 231)),
    ((1214, 1218), (234, 234)),
    ((1220, 1226), (236, 236)),
    ((1227, 1234), (237, 237)),
    ((1247, 1251), (240, 240)),
    ((1253, 1259), (242, 242)),
    ((1260, 1267), (243, 243)),
    ((1280, 1284), (246, 246)),
    ((1286, 1292), (248, 248)),
    ((1293, 1300), (249, 249)),
    ((1313, 1317), (252, 252)),
    ((1319, 1325), (254, 254)),
    ((1326, 1333), (255, 255)),
    ((1346, 1350), (258, 258)),
    ((1352, 1358), (260, 260)),
    ((1359, 1366), (261, 261)),
    ((1379, 1383), (264, 264)),
    ((1385, 1391), (266, 266)),
    ((1392, 1399), (267, 267)),
    ((1412, 1416), (270, 270)),
    ((1418, 1424), (272, 272)),
    ((1425, 1432), (273, 273)),
    ((1445, 1449), (276, 276)),
    ((1451, 1457), (278, 278)),
    ((1458, 1465), (279, 279)),
    ((1478, 1482), (282, 282)),
    ((1484, 1490), (284, 284)),
    ((1491, 1498), (285, 285)),
    ((1511, 1515), (288, 288)),
    ((1517, 1523), (290, 290)),
    ((1524, 1531), (291, 291)),
    ((1544, 1548), (294, 294)),
    ((1550, 1556), (296, 296)),
    ((1557, 1564), (297, 297)),
    ((1577, 1581), (300, 300)),
    ((1583, 1589), (302, 302)),
    ((1590, 1597), (303, 303)),
    ((1610, 1614), (306, 306)),
    ((1616, 1622), (308, 308)),
    ((1623, 1630), (309, 309)),
    ((1643, 1647), (312, 312)),
    ((1649, 1655), (314, 314)),
    ((1656, 1663), (315, 315)),
    ((1676, 1680), (318, 318)),
    ((1682, 1688), (320, 320)),
    ((1689, 1696), (321, 321)),
    ((1709, 1713), (324, 324)),
    ((1715, 1721), (326, 326)),
    ((1722, 1729), (327, 327)),
    ((1742, 1746), (330, 330)),
    ((1748, 1754), (332, 332)),
    ((1755, 1762), (333, 333)),
    ((1775, 1779), (336, 336)),
    ((1781, 1787), (338, 338)),
    ((1788, 1795), (339, 339)),
    ((1808, 1812), (342, 342)),
    ((1814, 1820), (344, 344)),
    ((1821, 1828), (345, 345)),
    ((1841, 1845), (348, 348)),
    ((1847, 1853), (350, 350)),
    ((1854, 1861), (351, 351)),
    ((1874, 1878), (354, 354)),
    ((1880, 1886), (356, 356)),
    ((1887, 1894), (357, 357)),
    ((1907, 1911), (360, 360)),
    ((1913, 1919), (362, 362)),
    ((1920, 1927), (363, 363)),
    ((1940, 1944), (366, 366)),
    ((1946, 1952), (368, 368)),
    ((1953, 1960), (369, 369)),
    ((1973, 1977), (372, 372)),
    ((1979, 1985), (374, 374)),
    ((1986, 1993), (375, 375)),
)
