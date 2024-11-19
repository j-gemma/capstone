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
    ((14, 18), (8, 8)),
    ((20, 27), (10, 10)),
    ((40, 44), (13, 13)),
    ((46, 55), (15, 15)),
    ((56, 63), (16, 16)),
    ((64, 70), (17, 17)),
    ((71, 77), (18, 18)),
    ((90, 94), (27, 27)),
    ((96, 103), (29, 29)),
    ((104, 110), (30, 30)),
    ((123, 127), (33, 33)),
    ((129, 136), (35, 35)),
    ((137, 144), (36, 36)),
    ((145, 152), (37, 37)),
    ((165, 169), (40, 40)),
    ((171, 179), (42, 42)),
    ((180, 188), (43, 43)),
    ((201, 205), (46, 46)),
    ((207, 215), (48, 48)),
    ((216, 224), (49, 49)),
    ((237, 241), (52, 52)),
    ((243, 249), (54, 54)),
    ((262, 266), (57, 57)),
    ((268, 274), (59, 59)),
    ((287, 291), (62, 62)),
    ((293, 300), (64, 64)),
    ((313, 317), (67, 67)),
    ((319, 326), (69, 69)),
    ((339, 343), (72, 72)),
    ((345, 351), (74, 74)),
    ((352, 359), (75, 75)),
    ((372, 376), (78, 78)),
    ((378, 384), (80, 80)),
    ((385, 392), (81, 81)),
    ((405, 409), (84, 84)),
    ((411, 417), (86, 86)),
    ((418, 425), (87, 87)),
    ((438, 442), (90, 90)),
    ((444, 450), (92, 92)),
    ((451, 458), (93, 93)),
    ((471, 475), (96, 96)),
    ((477, 483), (98, 98)),
    ((484, 491), (99, 99)),
    ((504, 508), (102, 102)),
    ((510, 516), (104, 104)),
    ((517, 524), (105, 105)),
    ((537, 541), (108, 108)),
    ((543, 549), (110, 110)),
    ((550, 557), (111, 111)),
    ((570, 574), (114, 114)),
    ((576, 582), (116, 116)),
    ((583, 590), (117, 117)),
    ((603, 607), (120, 120)),
    ((609, 615), (122, 122)),
    ((616, 623), (123, 123)),
    ((636, 640), (126, 126)),
    ((642, 648), (128, 128)),
    ((649, 656), (129, 129)),
    ((669, 673), (132, 132)),
    ((675, 681), (134, 134)),
    ((682, 689), (135, 135)),
    ((702, 706), (138, 138)),
    ((708, 714), (140, 140)),
    ((715, 722), (141, 141)),
    ((735, 739), (144, 144)),
    ((741, 747), (146, 146)),
    ((748, 755), (147, 147)),
    ((768, 772), (150, 150)),
    ((774, 780), (152, 152)),
    ((781, 788), (153, 153)),
    ((801, 805), (156, 156)),
    ((807, 813), (158, 158)),
    ((814, 821), (159, 159)),
    ((834, 838), (162, 162)),
    ((840, 846), (164, 164)),
    ((847, 854), (165, 165)),
    ((867, 871), (168, 168)),
    ((873, 879), (170, 170)),
    ((880, 887), (171, 171)),
    ((900, 904), (174, 174)),
    ((906, 912), (176, 176)),
    ((913, 920), (177, 177)),
    ((933, 937), (180, 180)),
    ((939, 945), (182, 182)),
    ((946, 953), (183, 183)),
    ((966, 970), (186, 186)),
    ((972, 978), (188, 188)),
    ((979, 986), (189, 189)),
    ((999, 1003), (192, 192)),
    ((1005, 1011), (194, 194)),
    ((1024, 1028), (197, 197)),
    ((1030, 1036), (199, 199)),
    ((1037, 1044), (200, 200)),
    ((1057, 1061), (203, 203)),
    ((1063, 1069), (205, 205)),
    ((1082, 1086), (208, 208)),
    ((1088, 1094), (210, 210)),
    ((1095, 1102), (211, 211)),
    ((1115, 1119), (214, 214)),
    ((1121, 1127), (216, 216)),
    ((1128, 1135), (217, 217)),
    ((1148, 1152), (220, 220)),
    ((1154, 1160), (222, 222)),
    ((1161, 1168), (223, 223)),
    ((1181, 1185), (226, 226)),
    ((1187, 1193), (228, 228)),
    ((1194, 1201), (229, 229)),
    ((1214, 1218), (232, 232)),
    ((1220, 1226), (234, 234)),
    ((1227, 1234), (235, 235)),
    ((1247, 1251), (238, 238)),
    ((1253, 1259), (240, 240)),
    ((1260, 1267), (241, 241)),
    ((1280, 1284), (244, 244)),
    ((1286, 1292), (246, 246)),
    ((1293, 1300), (247, 247)),
    ((1313, 1317), (250, 250)),
    ((1319, 1325), (252, 252)),
    ((1326, 1333), (253, 253)),
    ((1346, 1350), (256, 256)),
    ((1352, 1358), (258, 258)),
    ((1359, 1366), (259, 259)),
    ((1379, 1383), (262, 262)),
    ((1385, 1391), (264, 264)),
    ((1392, 1399), (265, 265)),
    ((1412, 1416), (268, 268)),
    ((1418, 1424), (270, 270)),
    ((1425, 1432), (271, 271)),
    ((1445, 1449), (274, 274)),
    ((1451, 1457), (276, 276)),
    ((1458, 1465), (277, 277)),
    ((1478, 1482), (280, 280)),
    ((1484, 1490), (282, 282)),
    ((1491, 1498), (283, 283)),
    ((1511, 1515), (286, 286)),
    ((1517, 1523), (288, 288)),
    ((1524, 1531), (289, 289)),
    ((1544, 1548), (292, 292)),
    ((1550, 1556), (294, 294)),
    ((1557, 1564), (295, 295)),
    ((1577, 1581), (298, 298)),
    ((1583, 1589), (300, 300)),
    ((1590, 1597), (301, 301)),
    ((1610, 1614), (304, 304)),
    ((1616, 1622), (306, 306)),
    ((1623, 1630), (307, 307)),
    ((1643, 1647), (310, 310)),
    ((1649, 1655), (312, 312)),
    ((1656, 1663), (313, 313)),
    ((1676, 1680), (316, 316)),
    ((1682, 1688), (318, 318)),
    ((1689, 1696), (319, 319)),
    ((1709, 1713), (322, 322)),
    ((1715, 1721), (324, 324)),
    ((1722, 1729), (325, 325)),
    ((1742, 1746), (328, 328)),
    ((1748, 1754), (330, 330)),
    ((1755, 1762), (331, 331)),
    ((1775, 1779), (334, 334)),
    ((1781, 1787), (336, 336)),
    ((1788, 1795), (337, 337)),
    ((1808, 1812), (340, 340)),
    ((1814, 1820), (342, 342)),
    ((1821, 1828), (343, 343)),
    ((1841, 1845), (346, 346)),
    ((1847, 1853), (348, 348)),
    ((1854, 1861), (349, 349)),
    ((1874, 1878), (352, 352)),
    ((1880, 1886), (354, 354)),
    ((1887, 1894), (355, 355)),
    ((1907, 1911), (358, 358)),
    ((1913, 1919), (360, 360)),
    ((1920, 1927), (361, 361)),
    ((1940, 1944), (364, 364)),
    ((1946, 1952), (366, 366)),
    ((1953, 1960), (367, 367)),
    ((1973, 1977), (370, 370)),
    ((1979, 1985), (372, 372)),
    ((1986, 1993), (373, 373)),
)
