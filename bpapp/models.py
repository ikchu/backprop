# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

Operations = ['add', 'sub', 'mul', 'div', 'pow'] # add more if necessary
# what about unary operations like neg and exp?

class Node(models.Model): # private?
    # note: this automatically creates relationship from parent to children too
    # https://stackoverflow.com/questions/15486520/making-a-tree-structure-in-django-models
    l = models.OneToOneField('self', on_delete=models.CASCADE, null=True, related_name='lParent')
    r = models.OneToOneField('self', on_delete=models.CASCADE, null=True, related_name='rParent')
    op = models.CharField(max_length=10) # Operation type
    fp = models.FloatField(default=0) # Ground truth forward propagation value
    bp = models.FloatField(default=0) # Ground truth backward propagation value

    def __str__(self):
        return self.op +' '+ str(self.fp) +' '+ str(self.bp)

    def toShow(self):
        # if leaf
        if self.op == "v":
            return str(self.fp)
        else:
            return self.op

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.r is None and self.l is None:
            line = '%s' % (self.op + '|' + str(self.fp) + '|' + str(self.bp))
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only l child.
        if self.r is None:
            lines, n, p, x = self.l._display_aux()
            s = '%s' % (self.op + ' ' + str(self.fp) + '|' + str(self.bp))
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only r child.
        if self.l is None:
            lines, n, p, x = self.r._display_aux()
            s = '%s' % (self.op + ' ' + str(self.fp) + '|' + str(self.bp))
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        l, n, p, x = self.l._display_aux()
        r, m, q, y = self.r._display_aux()
        s = '%s' % (self.op + ' ' + str(self.fp) + '|' + str(self.bp))
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            l += [n * ' '] * (q - p)
        elif q < p:
            r += [m * ' '] * (p - q)
        zipped_lines = zip(l, r)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class Problem(models.Model): # default Django tutorial implementation
    question_text = models.CharField(max_length=200)
    root = models.OneToOneField(Node, on_delete=models.CASCADE, null=True, related_name='problem')

    # binary_expression_tree = (someRootNode)
    # hints = # reach feature, would need to put in a separate class and cross reference
    # comments = # reach feature, would need to put in a separate class and cross reference

    def __str__(self):
        if self.root is None:
            return self.question_text + ", " + "No Root"
        else:
            return self.question_text + ", " + self.root.op +' '+ str(round(self.root.fp, 2)) +' '+ str(round(self.root.bp, 2))