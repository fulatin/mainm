
from manimlib import *
import numpy as np

PROVE_TEXT_FONT_SIZE = 38
class Sine_Formula_of_two_angles_sum(Scene):
    def enter(self):
        tri = Polygon([0.,0.,0.],[0.,2.343,0.],[3.32,0.,0.])
        rect = Rectangle(0.2,0.2).set_x(0.1).set_y(0.1)
        arc = ArcBetweenPoints(np.array([3.,0.,0.,]),np.array([3.,0.5,0.])).flip().set_x(2.5)
        alpha= Tex("\\alpha").next_to(arc,LEFT).scale(0.9)
        a = Tex("a").next_to(tri,LEFT)
        b = Tex("b").next_to(tri,DOWN)
        c = Tex("c").next_to(tri,UR).move_to([2.,1.6,0.])
        group = VGroup(tri,rect,arc,alpha,a,b,c).set_x(-0.5).set_y(-0.2)
        for i in group:
            self.play(ShowCreation(i))
        # group.set_color_by_gradient([random_color(),random_bright_color()])
        group.generate_target()
        group.target.scale(0.8).move_to([-5,2,0])
        self.play(MoveToTarget(group))
        text = Tex("\\sin \\alpha = \\frac{a}{c}").set_color(RED)
        self.wait()
        self.play(Write(text))
        text.generate_target()
        text.target.move_to([-0.7,2.,0.])
        self.play(MoveToTarget(text))


        tri2 = Polygon([0.,0.,0.],[0.,2.343,0.],[3.32,0.,0.])     
        rect2 = Rectangle(0.2,0.2).set_x(0.1).set_y(0.1)
        arc2 = ArcBetweenPoints(np.array([3.,0.,0.,]),np.array([3.,0.5,0.])).flip().set_x(2.5)
        tempGroup = VGroup(tri2,rect2,arc2).stretch(0.5,1)
        beta= Tex("\\beta").next_to(arc2,LEFT).scale(0.7)
        d = Tex("d").next_to(tri2,LEFT)
        e = Tex("e").next_to(tri2,DOWN)
        f = Tex("f").next_to(tri2,UR).move_to([2.,1.6,0.])
        # group2 = VGroup(tri2,rect2,arc2,beta,d,e,f)
        group2 = VGroup(tempGroup,beta,d,e,f)

        
        group2.move_to([0,-1,0])
        for i in group2:
            self.play(Write(i))
        # group2.set_color_by_gradient([random_color(),random_bright_color()])
        group2.generate_target()
        group2.target.scale(0.8).move_to([-5,-2,0])
        self.play(MoveToTarget(group2))
        text2 = Tex("\\sin \\beta = \\frac{d}{f}").set_color(GREEN)
        self.wait()
        self.play(Write(text2))
        text2.generate_target()
        text2.target.move_to([-0.7,-2,0.])
        self.play(MoveToTarget(text2))



        question = Tex(r"\sin (\alpha+\beta) = ?").set_color(BLUE)
        question.scale(1.3)
        self.play(Write(question))
        self.wait(2)

        self.play(FadeOut(group),FadeOut(group2),FadeOut(text),FadeOut(text2))

        question.generate_target()
        question.target.scale(4)
        self.play(MoveToTarget(question))
        self.play(FadeOutToPoint(question,[0,0,0]))
        self.wait(2)

    def prove(self):
        tri = Polygon([1.,0.,0.],[0.,2.,0.],[-4.,0.,0.]).set_color(BLUE_B)
        self.play(ShowCreation(tri))
        # arc1 = Arc(np.pi-np.arctan(2),np.arctan(2),arc_center=RIGHT,radius = 0.3)
        # self.play(ShowCreation(arc1))
        line = Line([-2.4,0.8,0.],[1.,0.,0.]).set_color(RED)
        line2 = Line([-2.4,0.8,0.],[-2.4,0.,0.])
        self.play(ShowCreation(line),ShowCreation(line2))
        l1 = Line([-2.4,0.2,0.],[-2.2,0.2,0.])
        l2 = Line([-2.2,0.2,0.],[-2.2,0.,0.])
        self.play(ShowCreation(l1),ShowCreation(l2))
        rect  = Rectangle(0.2,0.2)
        rect.rotate(np.arctan(1/2)).move_to([0.09,2.,0.],aligned_edge=UR).set_color(BLUE_B)
        self.play(ShowCreation(rect))
        arc1 = Arc(np.pi-np.arctan(4/17),np.arctan(4/17),arc_center = np.array((1.,0.,0.)))
        arc2 = Arc(0,np.arctan(1/2),arc_center = np.array((-4.,0.,0.)),radius=0.4)
        arc3 = Arc(-np.arctan(4/17),np.arctan(4/17)+np.arctan(1/2),arc_center = np.array((-2.4,0.8,0.)),radius=0.4)
        alpha = Tex("\\alpha").scale(0.6).next_to(arc2).set_color(random_color()).shift([0.,0.1,0.])
        beta = Tex("\\beta").scale(0.6).next_to(arc1,LEFT).set_color(random_color()).shift([0.,0.05,0.])
        alphaAddBeta = Tex("\\alpha+\\beta").scale(0.6).next_to(arc3).set_color(random_color())
        pointsChars = VGroup(
            Tex("A").next_to(np.array([-4,0.,0.]),DOWN),
            Tex("B").next_to(np.array([1,0,0]),DOWN),
            Tex("C").next_to(np.array([0.,2.,0.]),UP),
            Tex("D").next_to(np.array([-2.4,0.8,0.]),UP),
            Tex("H").next_to(np.array([-2.4,0.,0.]),DOWN)
        )

        for i in pointsChars:
            i.set_color(random_color())
        self.wait(1)
        self.play(*[Write(i) for i in pointsChars] )
        self.wait(2)
        self.play(ShowCreation(arc1),ShowCreation(arc2),ShowCreation(arc3),ShowCreation(alpha),ShowCreation(beta),ShowCreation(alphaAddBeta))
        self.wait(2)
        triGroup = VGroup(tri,line,line2,l1,l2,rect,arc1,arc2,arc3,alpha,beta,alphaAddBeta,pointsChars)
        triGroup.generate_target()
        triGroup.target.move_to(np.array([-4.5,1.2,0.])).scale(0.7)
        self.play(MoveToTarget(triGroup))
        self.wait()
        prove_text_01 = Tex("\\because"," AH = AD \\cdot \\cos \\alpha "," \\qquad HB = BD \\cdot \\cos \\beta",font_size = PROVE_TEXT_FONT_SIZE)
        
        prove_text_01.shift([1,3.,0.])
        self.play(Write(prove_text_01))
        self.wait(4)

        prove_text_11 = Tex("\\therefore AB","=AH+HB","=AD \\cdot \\cos \\alpha + BD \\cdot \\cos \\beta",font_size = PROVE_TEXT_FONT_SIZE)
        prove_text_11[2].next_to(prove_text_11[1],DOWN,aligned_edge=LEFT)
        prove_text_11[0].next_to(prove_text_11[1],LEFT)
        prove_text_11.next_to(prove_text_01,DOWN,aligned_edge=LEFT)

        self.play(TransformMatchingShapes(VGroup(prove_text_01,pointsChars).copy(),prove_text_11))
        self.wait(7)

        prove_text_21 = Tex("\\therefore CB"," = AB \\cdot \\sin \\alpha ","= AD \\cdot \\cos \\alpha \\cdot \\sin \\alpha + BD \\cdot \\cos \\beta \\cdot \\sin \\alpha",font_size = PROVE_TEXT_FONT_SIZE)
        prove_text_21.next_to(prove_text_11,DOWN,aligned_edge=LEFT)
        prove_text_21[2].next_to(prove_text_21[1],DOWN,aligned_edge=LEFT)
        self.play(TransformMatchingShapes(prove_text_11.copy(),prove_text_21))
        self.wait(8)

        prove_text_31 = Tex("\\therefore \\sin (\\alpha + \\beta)",
                                                "=\\frac{CB}{BD}",
                                                "=\\frac{AD \\cdot \\cos \\alpha \\cdot \\sin \\alpha + BD \\cdot \\cos \\beta \\cdot \\sin \\alpha}{BD}",
                                                "=","\\frac{AD}{BD}","\\cdot \\cos \\alpha \\cdot \\sin \\alpha + \\cos \\beta \\cdot \\sin \\alpha",
                                                font_size = PROVE_TEXT_FONT_SIZE)
        prove_text_31[4].set_color(RED_A)
        prove_text_31[2].next_to(prove_text_31[1],DOWN,aligned_edge=LEFT)
        prove_text_31[3].next_to(prove_text_31[2],DOWN,aligned_edge=LEFT)
        prove_text_31[4].next_to(prove_text_31[3],RIGHT)
        prove_text_31[5].next_to(prove_text_31[4],RIGHT)

        prove_text_31.next_to(prove_text_21,DOWN,aligned_edge=LEFT)
        self.play(TransformMatchingShapes(prove_text_21.copy(),prove_text_31))
        self.wait(9)


        prove_text_41 = Tex(" \\because  AD = \\frac{DH}{\\sin \\alpha}"," \\qquad BD = \\frac{DH}{\\sin \\beta}",font_size = PROVE_TEXT_FONT_SIZE).shift([1,3.,0.])
        self.play(FadeOut(VGroup(prove_text_01,prove_text_11,prove_text_21,prove_text_31),UP))
        self.wait(1)
        self.play(Write(prove_text_41))
        self.wait(5)


        prove_text_51 = Tex("\\therefore \\frac{AD}{BD} = \\frac{\\sin \\beta}{\\sin \\alpha}",font_size = PROVE_TEXT_FONT_SIZE)
        prove_text_51.next_to(prove_text_41,DOWN,aligned_edge=LEFT)
        self.play(TransformMatchingShapes(prove_text_41.copy(),prove_text_51))
        self.wait(5)


        prove_text_61 = Tex("\\therefore \\sin (\\alpha + \\beta)","=\\frac{\\sin \\beta}{\\sin \\alpha} \\cdot \\cos \\alpha \\cdot \\sin \\alpha + \\cos \\beta \\cdot \\sin \\alpha",
                                                                   "=\\sin \\beta \\cdot \\cos \\alpha+\\cos \\beta \\cdot \\sin \\alpha",font_size = PROVE_TEXT_FONT_SIZE)
        prove_text_61[0].next_to(prove_text_61[1],LEFT)
        prove_text_61[2].next_to(prove_text_61[1],DOWN,aligned_edge=LEFT)
        prove_text_61.next_to(prove_text_51,DOWN,aligned_edge=LEFT)
        self.play(TransformMatchingShapes(prove_text_51.copy(),prove_text_61))
        self.wait(9)


        res = Tex("\\sin (\\alpha + \\beta) = \\sin \\beta \\cdot \\cos \\alpha+\\cos \\beta \\cdot \\sin \\alpha").scale(1.5).set_color(BLUE_B)
        self.play(TransformMatchingShapes(VGroup(prove_text_41,triGroup,prove_text_51,prove_text_61),res))
        self.wait(5)
        self.play(FadeOut(res,UP))
        self.wait(6)
    
    def construct(self):
        self.enter()
        self.prove()
