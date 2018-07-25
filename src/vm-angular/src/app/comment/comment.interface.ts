import { Reply } from './reply.interface';

export interface Comment {
	show_replies: boolean;
	text: string;
	username: string;
	id: string;
	reply: Reply[];
}
